from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from invitations.models import Invitation
from invitations.constants import InviteStatus

User = get_user_model()


def validate_invite_owner(user: User, invite: Invitation) -> None:
    if invite.invitee != user:
        raise PermissionError("You're not allowed to respond to this invite!")


def validate_status(status: int) -> None:
    if status not in InviteStatus.RESPONDS:
        raise ValidationError("Wrong status choose right one!")


def validate_self_friend_request(*, sender: User, target: User) -> None:
    if sender == target:
        raise ValueError("Can't send friend request to yourself!")
