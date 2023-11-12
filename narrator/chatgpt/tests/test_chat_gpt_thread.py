import pytest

from narrator.chatgpt import ChatGpt


def test_chatgpt_thread_without_assistant(mock_openai_client):
    gpt = ChatGpt()
    with pytest.raises(RuntimeError):
        gpt.create_thread()


def test_chatgpt_create_thread(mock_openai_messages, mock_openai_threads):
    gpt = ChatGpt(assistant_id="test")
    gpt.create_thread(
        initial_messages=mock_openai_messages,
    )
    mock_openai_threads.create.assert_called_once_with(
        messages=[
            {"role": "system", "content": "test system message 1"},
            {"role": "user", "content": "test user message 1"},
        ]
    )


def test_chatgpt_append_thread_message_without_thread(mock_openai_client):
    gpt = ChatGpt()
    with pytest.raises(RuntimeError):
        gpt.append_message_to_thread(content="test user message 1", thread_id="")


def test_chatgpt_append_thread_message(mock_openai_messages, mock_openai_threads):
    gpt = ChatGpt(assistant_id="test")
    gpt.append_message_to_thread(
        thread_id="!@#123",
        content="test user message 1",
    )
    mock_openai_threads.messages.create.assert_called_once_with(
        content="test user message 1", role="user", thread_id="!@#123"
    )


def test_chatgpt_run_thread_without_assistant(mock_openai_client):
    gpt = ChatGpt()
    with pytest.raises(RuntimeError):
        gpt.run_thread(thread_id="!@#123")


def test_chatgpt_run_thread(mock_openai_client, mock_openai_threads):
    gpt = ChatGpt(assistant_id="test")
    gpt.run_thread(thread_id="!@#123")
    mock_openai_threads.runs.create.assert_called_once_with(
        assistant_id="test", thread_id="!@#123", instructions=""
    )

    gpt.run_thread(thread_id="!@#123", instructions="test instructions")
    mock_openai_threads.runs.create.assert_called_with(
        assistant_id="test", thread_id="!@#123", instructions="test instructions"
    )


def test_chatgpt_run_check_status(mock_openai_client):
    gpt = ChatGpt(assistant_id="test")
    gpt.check_run_status(run_id="!@#123", thread_id="!@#123")


@pytest.mark.skip("For debugging purposes only")
def test_chatgpt_run():
    # generic narrator assistant id
    gpt = ChatGpt(assistant_id="asst_ZJh7c8lOzcgZKBiKlAhaKCmn")
    thread = gpt.create_thread()

    gpt.append_message_to_thread(
        thread_id=thread.id,
        content="What is your name?",
    )
    run = gpt.run_thread(
        thread_id=thread.id,
        instructions="You are Avacyn!",
    )

    assert run
