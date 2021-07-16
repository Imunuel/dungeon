from django.contrib.auth import get_user_model
from django.db.models import QuerySet

from invitations.models import Invitation

User = get_user_model()


def get_user_invite(*, invite_id: int, user: User) -> Invitation:
    return Invitation.objects \
        .select_related('sender') \
        .select_related('invitee') \
        .get(pk=invite_id,
             invitee=user)


def get_user_invites(*, user: User) -> QuerySet[Invitation]:
    return Invitation.objects \
        .select_related('sender') \
        .filter(invitee=user) \
        .order_by('-created')
