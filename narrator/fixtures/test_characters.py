import pytest

from narrator.models import Character, CharacterInteraction


@pytest.fixture
def test_characters():
    """Test characters."""

    characters = Character.objects.bulk_create(
        [
            Character(
                first_name="John",
                last_name="Doe",
                voice="John Doe",
                is_player=False,
            ),
            Character(
                first_name="Jane",
                last_name="Doe",
                voice="Jane Doe",
                is_player=False,
            ),
            Character(
                first_name="John",
                last_name="Smith",
                voice="John Smith",
                is_player=False,
            ),
        ]
    )

    CharacterInteraction.objects.bulk_create(
        [
            CharacterInteraction(
                transmitter_character=characters[0],
                recipient_character=characters[1],
                text="Hello, how are you?",
                created_at="2021-01-01 00:00:00",
            ),
            CharacterInteraction(
                transmitter_character=characters[1],
                recipient_character=characters[0],
                text="I'm fine, thanks.",
                created_at="2021-01-01 00:00:01",
            ),
            CharacterInteraction(
                transmitter_character=characters[0],
                recipient_character=characters[1],
                text="What do you mean you are fine?",
                created_at="2021-01-01 00:00:02",
            ),
        ]
    )
    CharacterInteraction.objects.bulk_create(
        [
            CharacterInteraction(
                transmitter_character=characters[0],
                recipient_character=characters[2],
                text="What are we gonna eat? I am hungry.",
                created_at="2021-01-02 00:00:00",
            ),
            CharacterInteraction(
                transmitter_character=characters[2],
                recipient_character=characters[0],
                text="I don't know, maybe a burger?",
                created_at="2021-01-02 00:00:01",
            ),
        ]
    )

    return characters
