from rest_framework import viewsets

from narrator.models import Campaign
from narrator.serializers import CampaignSerializer


class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
