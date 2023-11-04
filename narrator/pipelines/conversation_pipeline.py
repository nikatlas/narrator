from typing import Any

from narrator.models import Character, CharacterInteraction
from narrator.modules.chat_gpt_module import ChatGptModule
from narrator.pipeline.pipeline import Pipeline
from narrator.pipeline.pipeline_context import PipelineContext


class ConversationPipeline(Pipeline):
    """
    A pipeline for summarizing company content.
    This pipeline is designed to automatically generate concise summaries of
    company web content centered around important domain keywords using ChatGpt.

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
                ChatGptModule(),
            ],
        )

    def pre_process(self, context: PipelineContext) -> Any:
        transmitter_character_pk = context.search_field("transmitter_character")
        recipient_character_pk = context.search_field("recipient_character")
        message = context.search_field("message")

        transmitter = Character.objects.get(pk=transmitter_character_pk)
        recipient = Character.objects.get(pk=recipient_character_pk)

        conversation_context = recipient.get_context(transmitter)
        context.add("resources", conversation_context["resources"])
        context.add("interactions", conversation_context["interactions"])

        context.add(
            "conversation",
            [
                *conversation_context["resources"],
                *conversation_context["interactions"],
                {
                    "role": "user",
                    "content": message,
                },
            ],
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
