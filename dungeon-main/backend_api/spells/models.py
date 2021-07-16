from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator

from polymorphic.models import PolymorphicModel

User = get_user_model()


class Spell(PolymorphicModel):
    name = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    cooldown = models.TimeField()
    is_default = models.BooleanField(default=False)


class HpChangingSpell(Spell):
    influence = models.IntegerField()
    is_healing = models.BooleanField(default=False)
    is_damaging = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if HpChangingSpell.influence < 0:
            HpChangingSpell.is_damaging = True
            return super(HpChangingSpell, self).save(*args, **kwargs)
        else:
            HpChangingSpell.is_healing = True
        return super(HpChangingSpell, self).save(*args, **kwargs)


class ArmorDecreasingSpell(Spell):
    reduction = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(1)], )


class UserSpell(models.Model):
    spell = models.ForeignKey(Spell, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_spell")
    is_on_cooldown = models.BooleanField(default=False)


class SpellPool(models.Model):
    first_slot = models.ForeignKey(UserSpell, on_delete=models.CASCADE, related_name="first_slot")
    second_slot = models.ForeignKey(UserSpell, on_delete=models.CASCADE, related_name="second_slot")
    third_slot = models.ForeignKey(UserSpell, on_delete=models.CASCADE, related_name="third_slot")
    fourth_slot = models.ForeignKey(UserSpell, on_delete=models.CASCADE, related_name="fourth_slot")
    fifth_slot = models.ForeignKey(UserSpell, on_delete=models.CASCADE, related_name="fifth_slot")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="spellpool")
