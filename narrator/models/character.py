from django.db import models
from django.db.models import Q

from .character_interaction import CharacterInteraction


class Character(models.Model):
    """Character model.

    Characters are the main actors of the story. They can be people, animals,
    objects or even concepts. They can be used to represent a person, a group
    of people, a place, an object, a concept, etc.
    """

    class Meta:
        """Meta class."""

        verbose_name = "Character"
        verbose_name_plural = "Characters"

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    voice = models.CharField(max_length=255)
    is_player = models.BooleanField(default=False)

    resources = models.ManyToManyField("Resource", related_name="characters")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_interactions(self, other_character):
        """Get character interactions with a specific character."""
        return CharacterInteraction.objects.filter(
            Q(recipient_character=self, transmitter_character=other_character)
            | Q(recipient_character=other_character, transmitter_character=self)
        ).order_by("created_at")
