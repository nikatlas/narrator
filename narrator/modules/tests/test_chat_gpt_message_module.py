from unittest.mock import MagicMock, patch

import pytest

from narrator.modules.chat_gpt_message_module import ChatGptMessageModule
from narrator.modules.chat_gpt_module import ChatGptModule
from narrator.pipeline.pipeline_context import PipelineContext


@patch("narrator.modules.chat_gpt_message_module.isinstance", return_value=True)
def test_chat_gpt_message_module(mock_message_content_text, mock_openai_threads):
    payload = {
        "assistant_id": "test-assistant-id",
        "thread_id": "test-thread-id",
        "instructions": "test instructions",
        "message": "test message",
    }

    run_mock = MagicMock()
    run_mock.status = "complete"
    mock_openai_threads.runs.retrieve.return_value = run_mock

    mock_openai_threads.runs.create.return_value = MagicMock(status="queued")

    mock_openai_threads.messages.list.return_value = MagicMock(
        data=[MagicMock(content=[MagicMock(text=MagicMock(value="123"))])]
    )

    context = PipelineContext(payload=payload)
    gpt_module: ChatGptMessageModule = ChatGptMessageModule()
    module_output = gpt_module.run(context)
    assert module_output == "123"

    mock_openai_threads.messages.create.assert_called_once_with(
        thread_id="test-thread-id",
        role="user",
        content="test message",
    )

    mock_openai_threads.runs.create.assert_called_once_with(
        thread_id="test-thread-id",
        assistant_id="test-assistant-id",
        instructions="test instructions",
    )

    mock_openai_threads.runs.retrieve.assert_called_once_with(
        thread_id="test-thread-id",
        run_id=mock_openai_threads.runs.create.return_value.id,
    )


def test_chat_gpt_message_module_invalid_payload():
    bad_payload = 3.14
    context = PipelineContext(payload=bad_payload)
    bad_gpt_module: ChatGptModule = ChatGptModule()
    with pytest.raises(ValueError):
        bad_gpt_module.run(context)
