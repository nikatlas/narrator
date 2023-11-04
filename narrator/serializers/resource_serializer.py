from rest_framework import serializers

from narrator.models import Resource


class ResourceSerializer(serializers.HyperlinkedModelSerializer):
    """Resource serializer."""

    class Meta:
        model = Resource
        fields = ["name", "text"]
