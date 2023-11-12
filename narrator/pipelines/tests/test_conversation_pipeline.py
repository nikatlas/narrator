import pytest

from narrator.pipeline.pipeline_context import PipelineContext
from narrator.pipelines.conversation_pipeline import ConversationPipeline


def test_conversation_pipeline(mock_openai_chat_completion, test_characters):
    mock_response = {
        "choices": [
            {"message": {"role": "assistant", "content": "this is a mock message"}}
        ]
    }
    mock_openai_chat_completion.create.return_value = mock_response
    payload = {
        "transmitter_character": test_characters[0].pk,
        "recipient_character": test_characters[1].pk,
        "message": "this is a mock question",
    }

    context = PipelineContext(payload=payload)
    conversation_pipeline = ConversationPipeline(context=context)
    pipeline_output = conversation_pipeline.run()
    assert pipeline_output.result == "this is a mock message"

    interactions = test_characters[0].get_interactions(test_characters[1])
    assert interactions.count() == 5
    assert interactions[3].text == "this is a mock question"
    assert interactions[4].text == "this is a mock message"

    other_interactions = test_characters[1].get_interactions(test_characters[0])
    assert other_interactions.count() == 5
    assert interactions[3].text == "this is a mock question"
    assert interactions[4].text == "this is a mock message"

    assert len(mock_openai_chat_completion.create.mock_calls) == 1
    mock_openai_chat_completion.create.assert_called_once_with(
        messages=[
            {
                "role": "user",
                "content": "Hello, how are you?",
            },
            {
                "role": "assistant",
                "content": "I'm fine, thanks.",
            },
            {
                "role": "user",
                "content": "What do you mean you are fine?",
            },
            {
                "role": "user",
                "content": "this is a mock question",
            },
        ],
        temperature=1.0,
        max_tokens=200,
        top_p=0.95,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        model="gpt-4-1106-preview",
    )


def test_conversation_pipeline_with_resources(
    mock_openai_chat_completion, test_characters, test_resources
):
    test_characters[1].resources.add(test_resources[0])
    test_characters[1].resources.add(test_resources[1])
    mock_response = {
        "choices": [
            {"message": {"role": "assistant", "content": "this is a mock message"}}
        ]
    }
    mock_openai_chat_completion.create.return_value = mock_response
    payload = {
        "transmitter_character": test_characters[0].pk,
        "recipient_character": test_characters[1].pk,
        "message": "this is a mock question",
    }

    context = PipelineContext(payload=payload)
    conversation_pipeline = ConversationPipeline(context=context)
    pipeline_output = conversation_pipeline.run()
    assert pipeline_output.result == "this is a mock message"

    interactions = test_characters[0].get_interactions(test_characters[1])
    assert interactions.count() == 5
    assert interactions[3].text == "this is a mock question"
    assert interactions[4].text == "this is a mock message"

    other_interactions = test_characters[1].get_interactions(test_characters[0])
    assert other_interactions.count() == 5
    assert interactions[3].text == "this is a mock question"
    assert interactions[4].text == "this is a mock message"

    assert len(mock_openai_chat_completion.create.mock_calls) == 1
    mock_openai_chat_completion.create.assert_called_once_with(
        messages=[
            {"role": "system", "content": "A tasty burger."},
            {"role": "system", "content": "A portion of fries."},
            {
                "role": "user",
                "content": "Hello, how are you?",
            },
            {
                "role": "assistant",
                "content": "I'm fine, thanks.",
            },
            {
                "role": "user",
                "content": "What do you mean you are fine?",
            },
            {
                "role": "user",
                "content": "this is a mock question",
            },
        ],
        temperature=1.0,
        max_tokens=200,
        top_p=0.95,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        model="gpt-4-1106-preview",
    )


@pytest.mark.skip(reason="Only for debugging actual api calls. No mocks here")
def test_conversation_pipeline_actual(test_characters, test_resources):
    test_characters[0].resources.add(test_resources[3])
    payload = {
        "transmitter_character": test_characters[1].pk,
        "recipient_character": test_characters[0].pk,
        "message": "I told you to go to the store and buy some milk.",
    }

    context = PipelineContext(payload=payload)
    conversation_pipeline = ConversationPipeline(context=context)
    pipeline_output = conversation_pipeline.run()
    print(f"\n\n{pipeline_output.result}\n\n")
