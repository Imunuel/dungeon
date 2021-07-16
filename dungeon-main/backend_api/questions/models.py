from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField()
    right_answer = models.CharField(max_length=255)

    class Meta:
        default_related_name = 'questions'

    def __str__(self):
        return f'{self.title}'
