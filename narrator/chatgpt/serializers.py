def serialize_resource(resource):
    """Serialise a resource.

    Args:
        resource (Resource): The resource.

    Returns:
        dict: The serialised resource.
    """
    return {
        "role": "system",
        "content": resource.text,
    }


def serialize_character_interaction(character, interaction):
    """Serialise a character interaction.

    Args:
        character (Character): The character.
        interaction (CharacterInteraction): The character interaction to
            serialise.

    Returns:
        dict: The serialised character interaction.
    """
    return {
        "role": "user" if interaction.recipient_character == character else "assistant",
        "content": interaction.text,
    }
