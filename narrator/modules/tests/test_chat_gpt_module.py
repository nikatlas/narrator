from unittest.mock import patch

import pytest

from narrator.modules.chat_gpt_module import ChatGptModule
from narrator.pipeline.pipeline_context import PipelineContext


@patch("narrator.chatgpt.chat_gpt.openai")
def test_chat_gpt_module(mock_openai):
    mock_response = {
        "choices": [
            {"message": {"role": "mock-role", "content": "this is a mock message"}}
        ]
    }
    mock_openai.ChatCompletion.create.return_value = mock_response

    payload = {
        "conversation": [
            {"message": {"role": "system", "content": "You are a robot."}},
        ]
    }

    context = PipelineContext(payload=payload)
    context.add("temperature", 2.0)
    context.add("prompt_index", 0)
    gpt_module: ChatGptModule = ChatGptModule()
    module_output = gpt_module.run(context)
    assert module_output == "this is a mock message"


def test_chat_gpt_module_invalid_payload():
    bad_payload = 3.14
    context = PipelineContext(payload=bad_payload)
    bad_gpt_module: ChatGptModule = ChatGptModule()
    with pytest.raises(ValueError):
        bad_gpt_module.run(context)
