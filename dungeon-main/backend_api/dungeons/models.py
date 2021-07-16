from django.db import models
from django.contrib.auth import get_user_model

from paths.models import Path


User = get_user_model()


class Dungeon(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    path = models.ForeignKey(
        to=Path,
        on_delete=models.CASCADE,
        related_name="dungeons",
    )
    position = models.PositiveIntegerField()
    image = models.ImageField(upload_to='images/dungeons/')

    class Meta:
        unique_together = [
            'path',
            'position',
        ]

    def __str__(self) -> str:
        return f'dungeon {self.title}'
