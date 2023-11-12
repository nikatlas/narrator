from typing import Any, Dict, List, Optional, Union

# Note: The openai-python library support for Azure OpenAI is in preview.
import openai
from openai import OpenAI
from openai._types import NOT_GIVEN, NotGiven
from openai.pagination import SyncCursorPage
from openai.types.beta import Assistant, Thread
from openai.types.beta.threads import Run, ThreadMessage

from narrator.constants import (
    OPEN_AI_VERSION,
    OPENAI_API_ENDPOINT,
    OPENAI_API_KEY,
    OPENAI_API_TYPE,
)

# TODO: Add support for the following:
# How to use embeddings to encode information:
# https://cookbook.openai.com/examples/question_answering_using_embeddings


Message = Dict[str, Any]


class ChatGpt:
    """ChatGpt communication class"""

    assistant_id: Optional[str] = None
    _client: Optional[OpenAI] = None

    def __init__(self, assistant_id: Optional[str] = None):
        self.set_openai_api()
        self.assistant_id = assistant_id

    @staticmethod
    def set_openai_api():
        openai.base_url = OPENAI_API_ENDPOINT
        openai.api_type = "azure" if OPENAI_API_TYPE == "azure" else "openai"
        openai.api_version = OPEN_AI_VERSION
        openai.api_key = OPENAI_API_KEY

    @staticmethod
    def get_output_from_response(response: Dict[str, Any]) -> List[Dict[str, Any]]:
        output_messages = []
        choices = response["choices"]
        for choice in choices:
            message = choice["message"]
            content = message["content"]
            role = message["role"]
            output_message = {"content": content, "role": role}
            output_messages.append(output_message)
        return output_messages

    @staticmethod
    def default_configuration(
        model: str = "gpt-4-1106-preview",
        temperature: float = 1.0,
        max_tokens: int = 200,
        top_p: float = 0.95,
        frequency_penalty: float = 0.0,
        presence_penalty: float = 0.0,
    ) -> Dict[str, Any]:
        return {
            "model": model,
            "temperature": temperature,
            "max_tokens": max_tokens,
            "top_p": top_p,
            "frequency_penalty": frequency_penalty,
            "presence_penalty": presence_penalty,
        }

    def request(self, messages: List[Dict[Any, Any]], **kwargs: Any) -> Any:
        try:
            return self.client.chat.completions.create(
                messages=messages,
                **{
                    **self.default_configuration(),
                    **kwargs,
                },
            )
        except Exception as exception:
            raise exception

    @property
    def client(self):
        if not self._client:
            self._client = OpenAI(
                api_key=OPENAI_API_KEY,
                base_url=OPENAI_API_ENDPOINT,
            )
        return self._client

    def create_assistant(
        self,
        name: str,
        description: Optional[str] = None,
        instructions: Optional[str] = None,
        file_ids: Optional[List[str]] = None,
    ) -> Assistant:
        if not name:
            raise RuntimeError("Name not specified.")
        if not instructions:
            instructions = """You are role-playing a character. Responds as if you
                 are that character with only the knowledge you have for your world and
                 nothing more. The knowledge about your character can be found in the
                 messages of the threads or the files attached to a thread or the
                 assistant. Global information should be hidden. The thoughts and
                 actions of the character should be spoken by a narrator and thus any
                 message you think that should be narrated should be annotated! If
                 the character is to speak annotate the message with the character
                 name!"""

        assistant: Assistant = self.client.beta.assistants.create(
            name=f"Narrator Character - {name}",
            description=description,
            instructions=instructions,
            tools=[{"type": "retrieval"}],
            model="gpt-4-1106-preview",
            file_ids=file_ids or [],
        )

        return assistant

    def update_assistant(
        self,
        assistant_id: str,
        description: Union[str, NotGiven] = NOT_GIVEN,
        instructions: Union[str, NotGiven] = NOT_GIVEN,
        file_ids: Union[List[str], NotGiven] = NOT_GIVEN,
    ) -> Assistant:
        if not assistant_id:
            raise RuntimeError("Assistant ID not specified.")

        assistant: Assistant = self.client.beta.assistants.update(
            assistant_id=assistant_id,
            description=description,
            instructions=instructions,
            file_ids=file_ids,
        )

        return assistant

    def create_thread(
        self,
        initial_messages: Optional[List[Message]] = None,
    ) -> Thread:
        if not self.assistant_id:
            raise RuntimeError("Assistant not specified.")

        thread: Thread = self.client.beta.threads.create(
            messages=initial_messages or [],
        )

        return thread

    def append_message_to_thread(
        self,
        thread_id: str,
        content: str,
    ) -> ThreadMessage:
        if not thread_id:
            raise RuntimeError("Thread ID not specified.")

        message: ThreadMessage = self.client.beta.threads.messages.create(
            thread_id=thread_id,
            role="user",
            content=content,
        )

        return message

    def run_thread(
        self,
        thread_id: str,
        instructions: str = "",
    ) -> Run:
        if not self.assistant_id:
            raise RuntimeError("Assistant not specified.")

        run: Run = self.client.beta.threads.runs.create(
            thread_id=thread_id,
            assistant_id=self.assistant_id,
            instructions=instructions,
        )

        return run

    def check_run_status(self, run_id: str, thread_id: str) -> Run:
        if not run_id or not thread_id:
            raise RuntimeError("Run ID or Thread ID not specified.")

        run: Run = self.client.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run_id,
        )

        return run

    def get_thread_messages(self, thread_id: str) -> SyncCursorPage[ThreadMessage]:
        list_messages: SyncCursorPage[
            ThreadMessage
        ] = self.client.beta.threads.messages.list(thread_id=thread_id)

        return list_messages
