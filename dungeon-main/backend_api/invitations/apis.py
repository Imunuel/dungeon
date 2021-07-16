from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authentication import (
    BasicAuthentication,
    SessionAuthentication
)

from common import mixins, throttling
from invitations import services, constants, selectors
from invitations.serializers import (
    FriendRequestsListSerializer,
    FriendRequestRespondSerializer,
    UserFriendRequestCreateSerializer
)

User = get_user_model()


class FriendRequestsListApi(APIView):
    """
    API that allows to list available friend requests of user.

    url = "/api/v1/users/<user>/friends/invites/

    <user> - target user

    Allowed method: GET
    """

    def get(self, request, user: User) -> Response:
        invites = selectors.get_user_invites(user=user)
        serializer = FriendRequestsListSerializer(invites, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class UserFriendRequestCreateApi(mixins.APIErrorsMixin, APIView):
    """
    API that allows to create friend request to specified user.

    url = "/api/v1/users/<user>/friends/invites/create

    <user> - target user

    Allowed method: POST

    Allowed fields and values:
    @message: str, less than 255 characters
    """
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated | IsAdminUser]
    throttle_classes = [throttling.FriendRequestRateThrottle]

    def post(self, request, user: User) -> Response:
        serializer = UserFriendRequestCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        services.create_invitation(sender=request.user,
                                   receiver=user,
                                   **serializer.validated_data)
        return Response(data={"message": constants.REQUEST_REPLY_MESSAGE},
                        status=status.HTTP_201_CREATED)


class FriendRequestRespondApi(mixins.APIErrorsMixin, APIView):
    """
    API that allows to create friend request to specified user.

    url = "/api/v1/users/<user>/friends/invites/respond

    <user> - target user

    Allowed method: PUT

    Allowed fields and values:
    @id: int, required, invitation id,
    @status: int, required, invitation status
    """
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated | IsAdminUser]

    def put(self, request, user: User) -> Response:
        serializer = FriendRequestRespondSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        invite = selectors.get_user_invite(user=user, invite_id=data["id"])

        message = services.respond_invitation(request.user,
                                              status=data["status"],
                                              invite=invite)
        return Response(data={"message": message}, status=status.HTTP_200_OK)
