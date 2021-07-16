from django.db import models
from django.utils.translation import gettext_lazy as _


class Level(models.Model):
    number = models.PositiveSmallIntegerField(_("Level number"), default=1)
    title = models.CharField(_('Title level'), max_length=255, default=_('Level_1'))
    exp = models.PositiveIntegerField(_('Exp level'), default=0)

    class Meta:
        verbose_name_plural = "Levels"

    def __str__(self):
        return f'Level {self.number}, exp {self.exp}'
