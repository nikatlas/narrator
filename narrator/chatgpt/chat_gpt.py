from typing import Any, Dict, List

# Note: The openai-python library support for Azure OpenAI is in preview.
import openai
from openai.error import ServiceUnavailableError

from narrator.constants import (
    OPEN_AI_VERSION,
    OPENAI_API_BASE,
    OPENAI_API_KEY,
    OPENAI_API_TYPE,
)
from narrator.utils import Singleton


class ChatGpt(metaclass=Singleton):
    """ChatGpt communication class"""

    def __init__(self):
        self.set_openai_api()

    @staticmethod
    def set_openai_api():
        if OPENAI_API_TYPE == "azure":
            openai.api_base = OPENAI_API_BASE
            openai.api_type = OPENAI_API_TYPE
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
    def default_configuration():
        return {
            "engine": "gpt35",
            "temperature": 1.0,
            "max_tokens": 200,
            "top_p": 0.95,
            "frequency_penalty": 0.0,
            "presence_penalty": 0.0,
        }

    def request(self, messages: List[Dict[Any, Any]], **kwargs: Any) -> Any:
        try:
            return openai.ChatCompletion.create(
                messages=messages, **{**self.default_configuration(), **kwargs}
            )
        except ServiceUnavailableError:
            return None
