from rest_framework import serializers

from narrator.models import Character


class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    """Character serializer."""

    class Meta:
        model = Character
        fields = ["first_name", "last_name", "voice", "is_player"]
