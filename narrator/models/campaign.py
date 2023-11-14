from django.contrib.auth.models import User
from django.db import models


class Campaign(models.Model):
    """Campaign model.

    Campaign is the root of world building. In campaigns places, characters
    and resources are attached. Campaigns are the main entry point for
    players.
    """

    class Meta:
        """Meta class."""

        verbose_name = "Campaign"
        verbose_name_plural = "Campaigns"

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    owner = models.ForeignKey(User, related_name="campaigns", on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
