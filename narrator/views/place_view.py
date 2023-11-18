from rest_framework import viewsets

from narrator.models import Place
from narrator.serializers import PlaceSerializer


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
