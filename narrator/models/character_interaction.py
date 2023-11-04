from django.db import models


class CharacterInteraction(models.Model):
    """Interaction model."""

    class Meta:
        """Meta class."""

        verbose_name = "Interaction"
        verbose_name_plural = "Interactions"

    transmitter_character = models.ForeignKey(
        "Character", related_name="character_transmissions", on_delete=models.CASCADE
    )
    recipient_character = models.ForeignKey(
        "Character", related_name="character_receptions", on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)
