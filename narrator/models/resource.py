from django.db import models


class Resource(models.Model):
    """Resource model.

    Resources are pieces of information that can be attached to characters.
    They can be used to provide additional information about a character,
    give world context and more.
    """

    class Meta:
        """Meta class."""

        verbose_name = "Resource"
        verbose_name_plural = "Resources"

    name = models.CharField(max_length=255)
    text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
