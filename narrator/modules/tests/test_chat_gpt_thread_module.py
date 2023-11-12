from unittest.mock import MagicMock

import pytest

from narrator.modules.chat_gpt_module import ChatGptModule
from narrator.modules.chat_gpt_thread_module import ChatGptThreadModule
from narrator.pipeline.pipeline_context import PipelineContext


def test_chat_gpt_thread_module(mock_openai_threads):
    mock_response = MagicMock()
    mock_response.id = "12344"
    mock_openai_threads.create.return_value = mock_response

    payload = {
        "assistant_id": "123",
        "initial_messages": [
            {"message": {"role": "system", "content": "You are a robot."}},
        ],
    }

    context = PipelineContext(payload=payload)
    gpt_module: ChatGptThreadModule = ChatGptThreadModule()
    module_output = gpt_module.run(context)
    assert module_output == "12344"

    mock_openai_threads.create.assert_called_once_with(
        messages=[{"message": {"role": "system", "content": "You are a robot."}}]
    )


def test_chat_gpt_thread_module_missing_assistant_id(mock_openai_threads):
    mock_response = MagicMock()
    mock_response.id = "12344"
    mock_openai_threads.create.return_value = mock_response

    payload = {
        "initial_messages": [
            {"message": {"role": "system", "content": "You are a robot."}},
        ]
    }

    context = PipelineContext(payload=payload)
    gpt_module: ChatGptThreadModule = ChatGptThreadModule()
    with pytest.raises(ValueError):
        gpt_module.run(context)


def test_chat_gpt_thread_module_invalid_payload():
    bad_payload = 3.14
    context = PipelineContext(payload=bad_payload)
    bad_gpt_module: ChatGptModule = ChatGptModule()
    with pytest.raises(ValueError):
        bad_gpt_module.run(context)
