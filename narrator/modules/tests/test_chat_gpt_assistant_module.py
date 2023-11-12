from unittest.mock import MagicMock

import pytest

from narrator.modules.chat_gpt_assistant_module import ChatGptAssistantModule
from narrator.modules.chat_gpt_module import ChatGptModule
from narrator.pipeline.pipeline_context import PipelineContext


def test_chat_gpt_assistant_module(mock_openai_assistant):
    mock_response = MagicMock()
    mock_response.id = "123"
    mock_openai_assistant.create.return_value = mock_response

    payload = {
        "id": "123",
        "name": "test-character",
        "description": "test description",
        "instructions": "test instructions",
        "file_ids": ["file-id-1", "file-id-2"],
    }

    context = PipelineContext(payload=payload)
    gpt_module: ChatGptAssistantModule = ChatGptAssistantModule()
    module_output = gpt_module.run(context)
    assert module_output == "123"

    mock_openai_assistant.create.assert_called_once_with(
        name="Narrator Character - test-character",
        instructions="test instructions",
        description="test description",
        tools=[{"type": "retrieval"}],
        model="gpt-4-1106-preview",
        file_ids=["file-id-1", "file-id-2"],
    )


def test_chat_gpt_assistant_module_invalid_payload():
    bad_payload = 3.14
    context = PipelineContext(payload=bad_payload)
    bad_gpt_module: ChatGptModule = ChatGptModule()
    with pytest.raises(ValueError):
        bad_gpt_module.run(context)
