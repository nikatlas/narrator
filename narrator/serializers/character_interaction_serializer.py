from rest_framework import serializers

from narrator.models import Character, CharacterInteraction


class CharacterRelatedField(serializers.PrimaryKeyRelatedField):
    def display_value(self, instance):
        return f"{instance.id} - {instance.first_name} {instance.last_name}"


class CharacterInteractionSerializer(serializers.HyperlinkedModelSerializer):
    """Character serializer."""

    queryset = CharacterInteraction.objects.prefetch_related("characters").order_by(
        "-created_at"
    )

    class Meta:
        model = CharacterInteraction
        fields = [
            "url",
            "id",
            "transmitter_character",
            "recipient_character",
            "text",
            "created_at",
        ]

    transmitter_character = CharacterRelatedField(
        queryset=Character.objects.all(),
    )
    recipient_character = CharacterRelatedField(
        queryset=Character.objects.all(),
    )
