from rest_framework import serializers

from narrator.models import Place


class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    """Place serializer."""

    queryset = Place.objects.all()

    class Meta:
        model = Place
        fields = [
            "url",
            "id",
            "name",
            "description",
        ]

    id = serializers.IntegerField(read_only=True)
