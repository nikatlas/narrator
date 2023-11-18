from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from narrator.views import (
    CampaignViewSet,
    CharacterInteractionViewSet,
    CharacterViewSet,
    ResourceViewSet,
    UserViewSet,
)

router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"campaign", CampaignViewSet)
router.register(r"character", CharacterViewSet)
router.register(r"character-interaction", CharacterInteractionViewSet)
router.register(r"resource", ResourceViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
