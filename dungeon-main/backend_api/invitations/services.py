from django.contrib.auth import get_user_model

from users import services
from invitations import validators
from invitations.models import Invitation
from invitations.constants import InviteStatus

User = get_user_model()


def create_invitation(sender: User, receiver: User, commentary: str) -> None:
    """
    Service that creates pending invite from user sender to user receiver
    """
    validators.validate_self_friend_request(sender=sender,
                                            target=receiver)
    Invitation.objects.create(sender=sender,
                              invitee=receiver,
                              commentary=commentary)


def respond_invitation(user: User, status: int, invite: Invitation) -> str:
    validators.validate_invite_owner(user=user, invite=invite)
    validators.validate_status(status=status)

    if status == InviteStatus.APPROVED:
        services.make_friendship(user, invite.sender)
    invite.status = status
    invite.save()
    return InviteStatus.RESPOND_MESSAGES[status].format(invite.sender.username)
