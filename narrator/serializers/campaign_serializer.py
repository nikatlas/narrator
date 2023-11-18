from rest_framework import serializers

from narrator.models import Campaign


class CampaignSerializer(serializers.HyperlinkedModelSerializer):
    """Campaign serializer."""

    queryset = Campaign.objects.prefetch_related("resources").all()

    class Meta:
        model = Campaign
        fields = [
            "url",
            "id",
            "name",
            "description",
            "owner",
        ]

    id = serializers.IntegerField(read_only=True)
