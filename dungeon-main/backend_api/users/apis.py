import jwt

from django.db import transaction

from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from users import services, selectors, permissions
from common import mixins
from common.utils import inline_serializer
from common.throttling import CreateUserRateThrottle
from common.serializers import FormattedDurationField, serializers

from users.serializers import (
    UserUpdatePasswordSerializer,
    UserFriendListSerializer,
    UserCreateSerializer,
    UserUpdateSerializer,
    )

User = get_user_model()


class UserCreateApi(mixins.APIErrorsMixin, APIView):
    """
    APIView reliable for user creation and
    prepopulation country field in user's profile.

    url = "/api/v1/users/create/

    Allowed method: POST

    Allowed fields and values:
    @username: str,
    @password: str,
    @location: str, abbreviation like, e.g "AS", "EU"
    """
    throttle_classes = [CreateUserRateThrottle]


    def post(self, request) -> Response:
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        with transaction.atomic():
            user = services.user_create(**serializer.validated_data)
            services.email_verification(request, user)
        return Response(status=status.HTTP_201_CREATED)


class UserUpdateApi(mixins.APIErrorsMixin, APIView):
    permission_classes = [IsAuthenticated & permissions.IsObjectOwner | IsAdminUser]

    def post(self, request, user: User) -> Response:
        serializer = UserUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        services.user_update(user=user, **serializer.validated_data)

        return Response(status=status.HTTP_200_OK)


class UserUpdatePasswordApi(mixins.APIErrorsMixin, APIView):
    """
    User's password update API

    """

    permission_classes = [IsAuthenticated & permissions.IsObjectOwner | IsAdminUser]



    def post(self, request, user: User) -> Response:
        serializer = UserUpdatePasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        services.user_update_password(user=user, **serializer.validated_data)

        return Response(status=status.HTTP_200_OK)


class UserFriendsListApi(mixins.APIErrorsMixin, APIView):
    """
    API reliable for friends listing.

    url = "/api/v1/users/<user>/friends/

    Allowed method: GET
    """

    def get(self, request, user: User) -> Response:
        friends = selectors.get_user_friends(user=user)
        serializer = UserFriendListSerializer(friends, many=True)
        return Response(data=serializer.data)


class VerifyEmail(mixins.APIErrorsMixin, APIView):
    """
    APIView reliable for verifying
    user's email.
    """

    def get(self, request) -> Response:
        token = request.GET.get('token')
        try:
            services.verify(token)
            return Response({'email': 'Successfully activated'}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError:
            return Response({'error': 'Activation Expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)


class UserDetailApi(mixins.APIErrorsMixin, APIView):
    permission_classes = [IsAuthenticated & permissions.IsObjectOwner | IsAdminUser]

    class OutputSerializer(serializers.ModelSerializer):
        profile = inline_serializer(fields={
            'server_location': serializers.CharField(),
            'level': serializers.CharField(),
        })

        class Meta:
            model = User
            fields = ('id', 'first_name', 'last_name', 'username', 'profile')

    def get(self, request, user: User) -> Response:
        detail = selectors.get_user_detail(user=user)
        serializer = self.OutputSerializer(detail)
        return Response(data=serializer.data)
