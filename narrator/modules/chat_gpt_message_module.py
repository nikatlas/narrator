from typing import Any, Dict

from time import sleep

from openai.pagination import SyncCursorPage
from openai.types.beta.threads import MessageContentText, ThreadMessage

from narrator.chatgpt.chat_gpt import ChatGpt
from narrator.pipeline import PipelineContext, PipelineModule

Input = Dict[str, Any]
Output = str


class ChatGptMessageModule(PipelineModule[Input, Output]):
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
        thread_id = context.search_field("thread_id")
        instructions = context.search_field("instructions", None)
        message = context.search_field("message", None)

        chat_gpt = ChatGpt(assistant_id=assistant_id)

        chat_gpt.append_message_to_thread(
            thread_id=thread_id,
            content=message,
        )

        run = chat_gpt.run_thread(
            thread_id=thread_id,
            instructions=instructions,
        )

        while run.status in ("queued", "in_progress"):
            sleep(0.1)
            run = chat_gpt.check_run_status(run.id, thread_id)

        context.add("run", run)
        context.add("status", run.status)

        messages: SyncCursorPage[ThreadMessage] = chat_gpt.get_thread_messages(
            thread_id
        )

        last_message = messages.data[0].content[0]

        response: str = ""
        if isinstance(last_message, MessageContentText):
            response = last_message.text.value

        context.add("response", response)
        context.add("thread_messages", messages.data[:5])
        return response
