from django.db import models


class Path(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self) -> str:
        return self.title
