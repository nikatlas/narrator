from unittest.mock import MagicMock, patch

import pytest

# pylint: disable=wildcard-import, unused-wildcard-import, redefined-outer-name
from .fixtures import *  # noqa


def pytest_collection_modifyitems(items):
    """Add django_db marker to all tests in order to use the test database."""
    for item in items:
        item.add_marker(pytest.mark.django_db(databases="__all__"))


###
# Mocks
###
@pytest.fixture
def mock_openai_messages():
    system_message = {
        "role": "system",
        "content": "test system message 1",
    }
    user_message = {
        "role": "user",
        "content": "test user message 1",
    }
    return [system_message, user_message]


@pytest.fixture
def mock_openai_client():
    with patch("narrator.chatgpt.chat_gpt.OpenAI") as mock_openai:
        yield mock_openai.return_value


@pytest.fixture
def mock_openai_chat_completion(mock_openai_client):
    mock_openai_completion = MagicMock()
    mock_openai_client.chat.completions = mock_openai_completion
    yield mock_openai_completion


@pytest.fixture
def mock_openai_threads(mock_openai_client):
    mock_openai_thread = MagicMock()
    mock_openai_client.beta.threads = mock_openai_thread
    yield mock_openai_thread


@pytest.fixture
def mock_openai_assistant(mock_openai_client):
    mock_openai_assistants = MagicMock()
    mock_openai_client.beta.assistants = mock_openai_assistants
    yield mock_openai_assistants
