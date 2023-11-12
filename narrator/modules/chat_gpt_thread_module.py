from typing import Any, Dict

from narrator.chatgpt.chat_gpt import ChatGpt
from narrator.pipeline import PipelineContext, PipelineModule

Input = Dict[str, Any]
Output = str


class ChatGptThreadModule(PipelineModule[Input, Output]):
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

        assistant_id = context.search_field("assistant_id")

        chat_gpt = ChatGpt(assistant_id=assistant_id)
        initial_messages = context.search_field("initial_messages", None)
        thread = chat_gpt.create_thread(
            initial_messages=initial_messages,
        )
        context.add("thread", thread)
        return thread.id
