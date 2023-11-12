from unittest.mock import MagicMock, patch

import pytest

from narrator.models import CharacterThread
from narrator.pipeline.pipeline_context import PipelineContext
from narrator.pipelines.thread_conversation_pipeline import ThreadConversationPipeline


@patch(
    "narrator.pipelines.thread_conversation_pipeline.ASSISTANT_ID", "test-assistant-id"
)
@patch("narrator.modules.chat_gpt_message_module.isinstance", return_value=True)
@patch("narrator.pipelines.thread_conversation_pipeline.ChatGptAssistantModule")
def test_thread_conversation_pipeline(
    mock_assistant_module, mock_isinstance, mock_openai_threads, test_characters
):
    run_mock = MagicMock()
    run_mock.status = "complete"
    mock_openai_threads.create.return_value = MagicMock(id="test-thread-id")
    mock_openai_threads.runs.retrieve.return_value = run_mock
    mock_openai_threads.runs.create.return_value = MagicMock(status="queued")
    mock_openai_threads.messages.list.return_value = MagicMock(
        data=[
            MagicMock(
                content=[
                    MagicMock(text=MagicMock(value="this is a mock message")),
                ]
            )
        ]
    )

    payload = {
        "transmitter_character": test_characters[0].pk,
        "recipient_character": test_characters[1].pk,
        "message": "this is a mock question",
    }

    context = PipelineContext(payload=payload)
    thread_conversation_pipeline = ThreadConversationPipeline(context=context)
    pipeline_output = thread_conversation_pipeline.run()
    assert pipeline_output.result == "this is a mock message"

    interactions = test_characters[0].get_interactions(test_characters[1])
    assert interactions.count() == 5
    assert interactions[3].text == "this is a mock question"
    assert interactions[4].text == "this is a mock message"

    other_interactions = test_characters[1].get_interactions(test_characters[0])
    assert other_interactions.count() == 5
    assert interactions[3].text == "this is a mock question"
    assert interactions[4].text == "this is a mock message"

    assert pipeline_output.search_field("skip") == ["chat_gpt_assistant"]

    mock_openai_threads.create.assert_called_once_with(
        messages=[],
    )

    mock_openai_threads.messages.create.assert_called_once_with(
        thread_id="test-thread-id",
        role="user",
        content="this is a mock question",
    )

    mock_openai_threads.runs.create.assert_called_once_with(
        thread_id="test-thread-id",
        assistant_id="test-assistant-id",
        instructions=ThreadConversationPipeline.get_instructions(
            test_characters[0],
            test_characters[1],
            [],
        ),
    )

    mock_openai_threads.runs.retrieve.assert_called_once_with(
        thread_id="test-thread-id",
        run_id=mock_openai_threads.runs.create.return_value.id,
    )


@patch(
    "narrator.pipelines.thread_conversation_pipeline.ASSISTANT_ID", "test-assistant-id"
)
@patch("narrator.modules.chat_gpt_message_module.isinstance", return_value=True)
def test_thread_conversation_pipeline_with_resources(
    mock_isinstance, mock_openai_threads, test_characters, test_resources
):
    test_characters[1].resources.add(test_resources[0])
    test_characters[1].resources.add(test_resources[1])
    run_mock = MagicMock()
    run_mock.status = "complete"
    mock_openai_threads.create.return_value = MagicMock(id="test-thread-id")
    mock_openai_threads.runs.retrieve.return_value = run_mock
    mock_openai_threads.runs.create.return_value = MagicMock(status="queued")
    mock_openai_threads.messages.list.return_value = MagicMock(
        data=[
            MagicMock(
                content=[
                    MagicMock(text=MagicMock(value="this is a mock message")),
                ]
            )
        ]
    )

    payload = {
        "transmitter_character": test_characters[0].pk,
        "recipient_character": test_characters[1].pk,
        "message": "this is a mock question",
    }

    context = PipelineContext(payload=payload)
    thread_conversation_pipeline = ThreadConversationPipeline(context=context)
    pipeline_output = thread_conversation_pipeline.run()
    assert pipeline_output.result == "this is a mock message"

    interactions = test_characters[0].get_interactions(test_characters[1])
    assert interactions.count() == 5
    assert interactions[3].text == "this is a mock question"
    assert interactions[4].text == "this is a mock message"

    other_interactions = test_characters[1].get_interactions(test_characters[0])
    assert other_interactions.count() == 5
    assert interactions[3].text == "this is a mock question"
    assert interactions[4].text == "this is a mock message"

    mock_openai_threads.create.assert_called_once_with(
        messages=[],
    )

    mock_openai_threads.messages.create.assert_called_once_with(
        thread_id="test-thread-id",
        role="user",
        content="this is a mock question",
    )

    mock_openai_threads.runs.create.assert_called_once_with(
        thread_id="test-thread-id",
        assistant_id="test-assistant-id",
        instructions=ThreadConversationPipeline.get_instructions(
            test_characters[0],
            test_characters[1],
            [
                {
                    "role": "system",
                    "content": "A tasty burger.",
                },
                {
                    "role": "system",
                    "content": "A portion of fries.",
                },
            ],
        ),
    )

    mock_openai_threads.runs.retrieve.assert_called_once_with(
        thread_id="test-thread-id",
        run_id=mock_openai_threads.runs.create.return_value.id,
    )

    CharacterThread.objects.get(
        thread_id="test-thread-id",
        transmitter_character=test_characters[0],
        recipient_character=test_characters[1],
    )


@pytest.mark.skip(reason="Only for debugging actual api calls. No mocks here")
def test_thread_conversation_pipeline_actual(test_characters, test_resources):
    test_characters[0].resources.add(test_resources[3])
    payload = {
        "transmitter_character": test_characters[1].pk,
        "recipient_character": test_characters[0].pk,
        "message": "I told you to go to the store and buy some milk.",
    }

    context = PipelineContext(payload=payload)
    conversation_pipeline = ThreadConversationPipeline(context=context)
    pipeline_output = conversation_pipeline.run()
    print(f"\n\n{pipeline_output.result}\n\n")


@patch(
    "narrator.pipelines.thread_conversation_pipeline.ASSISTANT_ID", "test-assistant-id"
)
@patch("narrator.modules.chat_gpt_message_module.isinstance", return_value=True)
@patch("narrator.pipelines.thread_conversation_pipeline.ChatGptAssistantModule")
def test_thread_conversation_with_existing_thread_skip_thread_step(
    mock_assistant_module, mock_isinstance, mock_openai_threads, test_characters
):
    CharacterThread.objects.create(
        thread_id="test-thread-id",
        transmitter_character=test_characters[0],
        recipient_character=test_characters[1],
    )
    run_mock = MagicMock()
    run_mock.status = "complete"
    mock_openai_threads.runs.retrieve.return_value = run_mock
    mock_openai_threads.runs.create.return_value = MagicMock(status="queued")
    mock_openai_threads.messages.list.return_value = MagicMock(
        data=[
            MagicMock(
                content=[
                    MagicMock(text=MagicMock(value="this is a mock message")),
                ]
            )
        ]
    )

    payload = {
        "transmitter_character": test_characters[0].pk,
        "recipient_character": test_characters[1].pk,
        "message": "this is a mock question",
    }

    context = PipelineContext(payload=payload)
    thread_conversation_pipeline = ThreadConversationPipeline(context=context)
    pipeline_output = thread_conversation_pipeline.run()
    assert pipeline_output.result == "this is a mock message"

    interactions = test_characters[0].get_interactions(test_characters[1])
    assert interactions.count() == 5
    assert interactions[3].text == "this is a mock question"
    assert interactions[4].text == "this is a mock message"

    other_interactions = test_characters[1].get_interactions(test_characters[0])
    assert other_interactions.count() == 5
    assert interactions[3].text == "this is a mock question"
    assert interactions[4].text == "this is a mock message"

    assert pipeline_output.search_field("skip") == [
        "chat_gpt_assistant",
        "chat_gpt_thread",
    ]

    mock_openai_threads.create.assert_not_called()
    mock_openai_threads.messages.create.assert_called_once_with(
        thread_id="test-thread-id",
        role="user",
        content="this is a mock question",
    )

    mock_openai_threads.runs.create.assert_called_once_with(
        thread_id="test-thread-id",
        assistant_id="test-assistant-id",
        instructions=ThreadConversationPipeline.get_instructions(
            test_characters[0],
            test_characters[1],
            [],
        ),
    )

    mock_openai_threads.runs.retrieve.assert_called_once_with(
        thread_id="test-thread-id",
        run_id=mock_openai_threads.runs.create.return_value.id,
    )
