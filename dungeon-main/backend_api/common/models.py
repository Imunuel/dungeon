from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

__all__ = [
    "models",
    "TimestampedModel"
]


class TimestampedModel(models.Model):
    """
        An abstract behavior model representing timestamping a model with:
        `created` field,
        `modified` field.
    """
    created = models.DateTimeField(auto_now_add=True,
                                   db_index=True,
                                   verbose_name=_("Created at"))
    modified = models.DateTimeField(db_index=True,
                                    null=True,
                                    blank=True,
                                    verbose_name=_("Modified at"))

    class Meta:
        abstract = True

    @property
    def changed(self) -> bool:
        return bool(self.modified)

    def save(self, *args, **kwargs):
        if self.pk:
            self.modified = timezone.now()
        return super().save(*args, **kwargs)
