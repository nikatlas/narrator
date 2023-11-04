class ResourceSerializer:
    """Character interaction serializer."""

    @staticmethod
    def serialize(resource):
        """Serialise a character interaction.

        Args:
            resource (Resource): The resource.

        Returns:
            dict: The serialised resource.
        """
        return {
            "role": "system",
            "content": resource.text,
        }
