from django.db import models

from dungeons.models import Dungeon


class Floor(models.Model):
    title = models.CharField(max_length=250, blank=False, null=False)
    position = models.PositiveIntegerField()
    dungeon = models.ForeignKey(to=Dungeon, on_delete=models.CASCADE, related_name='floors')
    given_exp = models.PositiveIntegerField()
    is_last = models.BooleanField()

    def save(self, *args, **kwargs):
        if not self.is_last:
            return super(Floor, self).save(*args, **kwargs)
        Floor.objects \
            .filter(is_last=True, dungeon_id=self.dungeon_id) \
            .update(is_last=False)
        return super(Floor, self).save(*args, **kwargs)
