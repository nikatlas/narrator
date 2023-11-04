from rest_framework import viewsets

from narrator.models import Resource
from narrator.serializers import ResourceSerializer


class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
