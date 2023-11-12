import pytest
from openai._types import NOT_GIVEN

from narrator.chatgpt import ChatGpt


def test_chatgpt_assistant_no_name():
    gpt = ChatGpt()
    with pytest.raises(RuntimeError):
        gpt.create_assistant(name="", instructions="test instructions")


def test_chatgpt_assistant(mock_openai_assistant):
    gpt = ChatGpt()

    gpt.create_assistant(
        name="test-character",
        instructions="test instructions",
        file_ids=["file-id-1", "file-id-2"],
    )

    mock_openai_assistant.create.assert_called_once_with(
        name="Narrator Character - test-character",
        instructions="test instructions",
        tools=[{"type": "retrieval"}],
        model="gpt-4-1106-preview",
        file_ids=["file-id-1", "file-id-2"],
    )


def test_chatgpt_assistant_update(mock_openai_assistant):
    gpt = ChatGpt()

    gpt.update_assistant(
        assistant_id="test",
        instructions="test instructions",
        file_ids=["file-id-1", "file-id-2"],
    )

    mock_openai_assistant.update.assert_called_once_with(
        assistant_id="test",
        description=NOT_GIVEN,
        instructions="test instructions",
        file_ids=["file-id-1", "file-id-2"],
    )


@pytest.mark.skip("For debugging only. No mocks here.")
def test_chatgpt_assistant_create():
    gpt = ChatGpt()
    gpt.create_assistant(
        name="test-character",
        instructions="test instructions 2",
        # file_ids=["file-id-1", "file-id-2"],
    )
