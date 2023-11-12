from typing import Any

from narrator.models import Character, CharacterInteraction
from narrator.modules.chat_gpt_assistant_module import ChatGptAssistantModule
from narrator.modules.chat_gpt_message_module import ChatGptMessageModule
from narrator.modules.chat_gpt_thread_module import ChatGptThreadModule
from narrator.pipeline.pipeline import Pipeline
from narrator.pipeline.pipeline_context import PipelineContext

ASSISTANT_ID = "asst_NE9pHFaan0JUBDUN6okDKRd5"


class ThreadConversationPipeline(Pipeline):
    """
    A pipeline for conversing through a thread and an assistant.

    @param context:Dict[str, Any] - contains input payload with a companies name,
    domain and keyword
    @return: str - summary
    """

    def __init__(
        self,
        context: PipelineContext,
    ):
        super().__init__(
            context,
            [
                ChatGptAssistantModule(),
                ChatGptThreadModule(),
                ChatGptMessageModule(),
            ],
        )

    def pre_process(self, context: PipelineContext) -> Any:
        transmitter_character_pk = context.search_field("transmitter_character")
        recipient_character_pk = context.search_field("recipient_character")
        message = context.search_field("message")
        context.merge("message", message)
        context.merge("transmitter_character", transmitter_character_pk)
        context.merge("recipient_character", recipient_character_pk)

        transmitter = Character.objects.get(pk=transmitter_character_pk)
        recipient = Character.objects.get(pk=recipient_character_pk)

        conversation_context = recipient.get_context(transmitter)

        context.add("resources", conversation_context["resources"])
        context.add("interactions", conversation_context["interactions"])

        # Assistant: First sample
        context.add("assistant_id", ASSISTANT_ID)
        skip = ["chat_gpt_assistant"]
        thread_id = context.search_field("thread_id", None)
        if thread_id:
            skip.append("chat_gpt_thread")
        context.add("skip", skip)

        context.add(
            "instructions",
            self.get_instructions(
                transmitter, recipient, conversation_context["resources"]
            ),
        )

        return context.payload

    def post_process(self, context: PipelineContext) -> Any:
        transmitter_character_pk = context.search_field("transmitter_character")
        recipient_character_pk = context.search_field("recipient_character")
        answer = context.result
        context.add("answer", answer)

        CharacterInteraction.objects.create(
            transmitter_character_id=transmitter_character_pk,
            recipient_character_id=recipient_character_pk,
            text=context.search_field("message"),
        )
        CharacterInteraction.objects.create(
            transmitter_character_id=recipient_character_pk,
            recipient_character_id=transmitter_character_pk,
            text=answer,
        )

        return context.result

    @staticmethod
    def get_instructions(transmitter, recipient, resources):
        instructions = (
            "You are role-playing a character."
            "Responds as if you are that character with only the knowledge you have "
            "for your world and nothing more. The knowledge about your character can "
            "be found in the messages of the threads or the files attached to a "
            "thread or the assistant. Global information should be hidden."
            f"Your character is {recipient.first_name} "
            f"{recipient.last_name} and you are talking to "
            f"{transmitter.first_name} {transmitter.last_name}."
            "The following are the resources you have available and specific to the "
            f"character {recipient.first_name} {recipient.last_name}: \n"
        )

        instructions += "\n\n".join([r["content"] for r in resources])

        return instructions
