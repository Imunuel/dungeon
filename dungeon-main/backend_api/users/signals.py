from django.db import transaction


from django.dispatch import receiver
from django.db.models import signals
from django.contrib.auth import get_user_model

from rest_framework.authtoken import models as auth_models

from users.models import Profile, FriendList
from levels.models import Level

User = get_user_model()


@transaction.atomic
@receiver(signals.post_save, sender=User)
def user_post_save(sender, instance, created, *args, **kwargs):
    if created:
        level = Level.objects.create()
        Profile.objects.create(user=instance, level=level)
        auth_models.Token.objects.create(user=instance)
        FriendList.objects.create(user=instance)
