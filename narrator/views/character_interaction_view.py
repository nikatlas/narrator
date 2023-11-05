from rest_framework import viewsets

from narrator.models import CharacterInteraction
from narrator.serializers import CharacterInteractionSerializer


class CharacterInteractionViewSet(viewsets.ModelViewSet):
    queryset = CharacterInteraction.objects.all()
    serializer_class = CharacterInteractionSerializer
