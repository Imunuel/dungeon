from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from common.models import TimestampedModel, models
from invitations.constants import InviteStatus

User = get_user_model()


class Invitation(TimestampedModel):
    sender = models.ForeignKey(User,
                               verbose_name=_("Invitation sender"),
                               related_name="sent_invites",
                               on_delete=models.CASCADE)
    invitee = models.ForeignKey(User,
                                verbose_name=_("Invitation receiver"),
                                related_name="received_invites",
                                on_delete=models.CASCADE)
    commentary = models.CharField(verbose_name=_("Invitation message"),
                                  max_length=255,
                                  null=True)
    status = models.IntegerField(verbose_name=_("Invitation state"),
                                 choices=InviteStatus.CHOICES,
                                 default=InviteStatus.PENDING)

    def __str__(self) -> str:
        return f"From {self.sender} to {self.invitee} is {self.status}"
