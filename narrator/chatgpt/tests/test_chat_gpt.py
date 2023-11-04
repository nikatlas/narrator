from typing import Any, List

from unittest.mock import patch

import openai
import pytest
from openai.error import ServiceUnavailableError

from narrator.chatgpt.chat_gpt import ChatGpt


@patch("narrator.chatgpt.chat_gpt.openai")
def test_chat_gpt(mock_openai):
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Does Azure OpenAI support customer managed keys?",
        },
        {
            "role": "assistant",
            "content": "Yes, customer managed keys are supported by Azure OpenAI.",
        },
        {
            "role": "user",
            "content": "Do other Azure Cognitive Services support this too?",
        },
    ]

    gpt = ChatGpt()
    gpt.request(messages, temperature=2.0)

    mock_openai.ChatCompletion.create.assert_called_once_with(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=2.0,
        max_tokens=200,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
    )


@patch("narrator.chatgpt.chat_gpt.openai")
def test_chat_gpt_default(mock_openai):
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
    ]

    gpt = ChatGpt()
    gpt.request(messages)

    mock_openai.ChatCompletion.create.assert_called_once_with(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=1.0,
        max_tokens=200,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
    )


@patch("narrator.chatgpt.chat_gpt.openai")
def test_chat_gpt_service_unavailable(mock_openai):
    mock_openai.ChatCompletion.create.side_effect = ServiceUnavailableError(
        "Service Unavailable"
    )
    messages: List[Any] = []
    gpt = ChatGpt()
    response = gpt.request(messages)
    assert response is None


@patch("narrator.chatgpt.chat_gpt.OPENAI_API_TYPE", "azure")
@patch("narrator.chatgpt.chat_gpt.OPENAI_API_KEY", "KEY_1")
@patch("narrator.chatgpt.chat_gpt.OPENAI_API_ENDPOINT", "ENDPOINT")
@patch("narrator.chatgpt.chat_gpt.OPEN_AI_VERSION", "2023-05-15")
def test_chat_gpt_openai_vars():
    gpt = ChatGpt()
    gpt.set_openai_api()
    assert openai.api_type == "azure"
    assert openai.api_key == "KEY_1"
    assert openai.api_base == "ENDPOINT"
    assert openai.api_version == "2023-05-15"


def test_output_from_gpt_response_function():
    gpt = ChatGpt()
    dummy_response = {
        "choices": [
            {
                "finish_reason": "stop",
                "index": 0,
                "message": {"role": "assistant", "content": "This is content"},
            }
        ]
    }
    assert gpt.get_output_from_response(dummy_response) == [
        {"role": "assistant", "content": "This is content"}
    ]


@pytest.mark.skip(reason="Only for debugging the actual api call. No mocks here.")
def test_chatgpt_request():
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
    ]

    gpt = ChatGpt()
    message = gpt.request(messages)
    assert message is None
