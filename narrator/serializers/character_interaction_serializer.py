class CharacterInteractionSerializer:
    """Character interaction serializer."""

    @staticmethod
    def serialize(character, interaction):
        """Serialise a character interaction.

        Args:
            character (Character): The character.
            interaction (CharacterInteraction): The character interaction to
                serialise.

        Returns:
            dict: The serialised character interaction.
        """
        return {
            "role": "user"
            if interaction.recipient_character == character
            else "assistant",
            "message": interaction.text,
        }
