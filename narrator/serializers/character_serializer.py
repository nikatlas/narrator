from rest_framework import serializers

from narrator.models import Character, Resource


class ResourcesRelatedField(serializers.PrimaryKeyRelatedField):
    def display_value(self, instance):
        return f"{instance.id} - {instance.name}"


class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    """Character serializer."""

    queryset = Character.objects.prefetch_related("resources").all()

    class Meta:
        model = Character
        fields = [
            "url",
            "id",
            "first_name",
            "last_name",
            "voice",
            "is_player",
            "resources",
            "resources_url",
        ]

    id = serializers.IntegerField(read_only=True)
    resources_url = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        source="resources",
        view_name="resource-detail",
    )
    resources = ResourcesRelatedField(
        many=True,
        required=False,
        queryset=Resource.objects.all(),
    )
