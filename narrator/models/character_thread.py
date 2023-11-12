from django.db import models


class CharacterThread(models.Model):
    """Interaction model."""

    class Meta:
        """Meta class."""

        verbose_name = "Thread"
        verbose_name_plural = "Threads"

    transmitter_character = models.ForeignKey(
        "Character",
        related_name="character_transmission_threads",
        on_delete=models.CASCADE,
    )
    recipient_character = models.ForeignKey(
        "Character",
        related_name="character_reception_threads",
        on_delete=models.CASCADE,
    )
    thread_id = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
