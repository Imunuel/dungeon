import pytest

from invitations.models import Invitation

pytestmark = [pytest.mark.django_db]


class TestInvitationSignals:
    """Testing invitation model signals"""

    def test_responded_invites_clear(self, user, another_user, invite):
        invite_id = invite.pk
        invite.status = 2

        invite.save()  # act

        assert not Invitation.objects.filter(pk=invite_id).exists()
