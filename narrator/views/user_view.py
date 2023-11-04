from django.contrib.auth.models import User
from rest_framework import viewsets

from narrator.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
