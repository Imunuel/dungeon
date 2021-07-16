from django.dispatch import receiver
from django.db.models import signals

from invitations.models import Invitation
from invitations.constants import InviteStatus


@receiver(signals.post_save, sender=Invitation)
def user_post_save(sender, instance, created, *args, **kwargs):
    if not created:
        if instance.status in InviteStatus.RESPONDS:
            instance.delete()
