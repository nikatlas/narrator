from rest_framework import serializers

from narrator.models import Place


class PlaceSerializer(serializers.ModelSerializer):
    """Place serializer."""

    queryset = Place.objects.all()

    class Meta:
        model = Place
        fields = ["url", "id", "name", "description", "resources"]

    id = serializers.IntegerField(read_only=True)
