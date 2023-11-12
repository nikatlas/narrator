from typing import Any, Dict

from narrator.chatgpt.chat_gpt import ChatGpt
from narrator.pipeline import PipelineContext, PipelineModule

Input = Dict[str, Any]
Output = str


class ChatGptAssistantModule(PipelineModule[Input, Output]):
    """Class for instantiating ChatGpt object"""

    def __init__(
        self,
        name: str = "chat_gpt_assistant",
        **kwargs: Any,
    ):
        super().__init__(name, **kwargs)

    def run(self, context: PipelineContext) -> Output:
        """
        Function that creates/update an assistant

        @param context: Dict[str, Any]
        @return: output_message: str - ChatGPT response
        """

        chat_gpt = ChatGpt()
        assistant_id = context.search_field("assistant_id", None)
        description = context.search_field("description", None)
        instructions = context.search_field("instructions", None)
        file_ids = context.search_field("file_ids", None)

        if assistant_id:
            assistant = chat_gpt.update_assistant(
                assistant_id=assistant_id,
                description=description,
                instructions=instructions,
                file_ids=file_ids,
            )
        else:
            assistant = chat_gpt.create_assistant(
                name=context.search_field("name"),
                description=description,
                instructions=instructions,
                file_ids=file_ids,
            )
        context.add("assistant", assistant)
        return assistant.id
