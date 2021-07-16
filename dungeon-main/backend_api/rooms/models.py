from django.db import models

from floors.models import Floor
from monsters.models import Monster
from questions.models import Question

from rooms import constants


class Room(models.Model):
    title = models.CharField(max_length=250, blank=False, null=False)
    description = models.CharField(max_length=250, blank=False, null=False)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE, related_name='rooms')
    position = models.PositiveIntegerField()
    room_type = models.CharField(max_length=50, default=constants.DEFAULT_ROOM, choices=constants.ROOMS_TYPES)
    is_last = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.is_last:
            return super(Room, self).save(*args, **kwargs)
        Room.objects \
            .filter(is_last=True, floor_id=self.floor_id) \
            .update(is_last=False)
        return super(Room, self).save(*args, **kwargs)


class MonsterRoom(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='monster_rooms')
    monster = models.ForeignKey(Monster, on_delete=models.CASCADE, related_name='monster_rooms')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='monster_rooms')
