from rest_framework import serializers

from narrator.models import Character, Resource


class ResourcesHyperlinkedRelatedField(serializers.HyperlinkedRelatedField):
    def display_value(self, instance):
        return f"{instance.id} - {instance.name}"


class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    """Character serializer."""

    queryset = Character.objects.prefetch_related("resources").all()

    class Meta:
        model = Character
        fields = ["url", "first_name", "last_name", "voice", "is_player", "resources"]

    resources = ResourcesHyperlinkedRelatedField(
        many=True,
        queryset=Resource.objects.all(),
        required=False,
        view_name="resource-detail",
    )
