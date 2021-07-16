from rest_framework import serializers

from common import utils
from common.serializers import FormattedDatetimeField
from invitations.constants import InviteStatus


class FriendRequestsListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    sender = utils.inline_serializer(
        fields={"username": serializers.CharField()}
    )
    sent_at = FormattedDatetimeField(source="created")


class UserFriendRequestCreateSerializer(serializers.Serializer):
    commentary = serializers.CharField(max_length=255)


class FriendRequestRespondSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    status = serializers.ChoiceField(
        required=True,
        choices=InviteStatus.RESPONDS
    )

