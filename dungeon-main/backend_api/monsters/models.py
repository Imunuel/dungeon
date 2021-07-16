from django.db import models

from monsters import constants


class Sprite(models.Model):
    image = models.ImageField(upload_to='images/sprites/')
    action = models.CharField(max_length=4, choices=constants.SPRITE_TYPES)

    def __str__(self):
        return f'{self.name}'


class Monster(models.Model):
    name = models.CharField(max_length=100)
    sprites = models.ManyToManyField(
        to=Sprite,
        through='MonsterSprites',
        through_fields=('monster', 'sprite')
    )

    def __str__(self):
        return f'{self.name} monster'


class MonsterSprites(models.Model):
    monster = models.ForeignKey(Monster, on_delete=models.CASCADE)
    sprite = models.ForeignKey(Sprite, on_delete=models.CASCADE)
