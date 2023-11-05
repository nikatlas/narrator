from rest_framework import serializers

from narrator.models import Character, CharacterInteraction


class CharacterHyperlinkedRelatedField(serializers.HyperlinkedRelatedField):
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
            "transmitter_character",
            "recipient_character",
            "text",
            "created_at",
        ]

    transmitter_character = CharacterHyperlinkedRelatedField(
        queryset=Character.objects.all(),
        view_name="character-detail",
    )
    recipient_character = CharacterHyperlinkedRelatedField(
        queryset=Character.objects.all(),
        view_name="character-detail",
    )
