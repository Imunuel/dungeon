from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Dialog(models.Model):
    users = models.ManyToManyField(
        to=User,
        through="DialogUser",
        through_fields=("dialog", "user")
    )

    def __str__(self) -> str:
        return f'{self.id}'


class DialogUser(models.Model):
    dialog = models.ForeignKey(
        to=Dialog,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )


class Message(models.Model):
    receiver = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="messages"
    )
    dialog = models.ForeignKey(
        to=Dialog,
        on_delete=models.CASCADE
    )
    datetime = models.DateTimeField(_("Date of creation"), auto_now_add=True)
    text = models.TextField(_("Message text"))
    is_read = models.BooleanField(_("Read"), default=False)

    class Meta:
        verbose_name_plural = "Messages"
        ordering = ("datetime", )
