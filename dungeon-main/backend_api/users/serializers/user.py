from rest_framework import serializers

from common.serializers import FormattedDurationField
from common.utils import inline_serializer


class UserCreateSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField()
    password = serializers.CharField()
    location = serializers.CharField()


class UserFriendListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()
    friends_for = FormattedDurationField()


class UserUpdateSerializer(serializers.Serializer):
    username = serializers.CharField(required=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    profile = inline_serializer(required=False, fields={
        "location": serializers.CharField()
    })


class UserUpdatePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(required=True)