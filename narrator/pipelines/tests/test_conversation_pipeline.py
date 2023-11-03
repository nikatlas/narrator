from unittest.mock import patch

from narrator.pipeline.pipeline_context import PipelineContext
from narrator.pipelines.conversation_pipeline import ConversationPipeline


@patch("narrator.chatgpt.chat_gpt.openai")
def test_conversation_pipeline(mock_openai):
    mock_response = {
        "choices": [
            {"message": {"role": "mock-role", "content": "this is a mock message"}}
        ]
    }
    mock_openai.ChatCompletion.create.return_value = mock_response
    payload = {
        "company_name": "apadua",
        "keyword": "cool",
        "domain": "apadua.de",
    }

    context = PipelineContext(payload=payload)
    conversation_pipeline = ConversationPipeline(context=context)
    pipeline_output = conversation_pipeline.run()
    assert pipeline_output.result == "this is a mock message"
