from django.db import models


class Place(models.Model):
    """Place model.

    Place is the root of world building. In campaigns places, characters
    and resources are attached. Places are the main entry point for
    players.
    """

    class Meta:
        """Meta class."""

        verbose_name = "Place"
        verbose_name_plural = "Places"

    name = models.CharField(max_length=255)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
