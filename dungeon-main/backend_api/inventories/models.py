from django.db import models
from polymorphic.models import PolymorphicModel
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save

from inventories import constants
from inventories.signals import create_user_inventory

User = get_user_model()


class DefaultStat(models.Model):
    agility = models.PositiveIntegerField(default=0)
    strength = models.PositiveIntegerField(default=0)
    intelligence = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True


class ArmorStat(models.Model):
    armor = models.PositiveIntegerField(default=0)
    extra_hp = models.PositiveIntegerField()

    class Meta:
        abstract = True


class Item(PolymorphicModel):
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField()
    is_active = models.BooleanField()

    def __str__(self):
        return f'{self.name} | {self.category}'


class Weapon(DefaultStat, Item):
    type = models.CharField(max_length=20, default=constants.KNIFE, choices=constants.WEAPON_TYPES)
    damage = models.PositiveIntegerField()
    attack_speed = models.PositiveIntegerField()
    vampirism = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(1)],)
    buff = models.CharField(max_length=20, default=constants.NONE, choices=constants.BUFF_TYPES)

    def __str__(self):
        return f'{self.type} Buff:{self.buff}'


class Helmet(ArmorStat, DefaultStat, Item):
    pass


class Shield(ArmorStat, Item):
    pass


class Pants(ArmorStat, DefaultStat, Item):
    pass


class Dress(ArmorStat, DefaultStat, Item):
    pass


class Boots(ArmorStat, DefaultStat, Item):
    pass


class Bracer(ArmorStat, DefaultStat, Item):
    pass


class Gauntlet(ArmorStat, DefaultStat, Item):
    pass


class Inventory(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )
    items = models.ManyToManyField(
        to=Item,
        through='InventoryItem',
        through_fields=('inventory', 'item')
    )

    class Meta:
        verbose_name = 'Inventory'
        verbose_name_plural = 'Inventories'

    def __str__(self):
        return f'{self.user.username} inventory'


class InventoryItem(models.Model):
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)


post_save.connect(create_user_inventory, sender=User)
