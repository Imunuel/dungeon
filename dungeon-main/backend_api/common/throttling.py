from rest_framework.throttling import AnonRateThrottle, UserRateThrottle


class FriendRequestRateThrottle(UserRateThrottle):
    scope = "friend-request"


class CreateUserRateThrottle(AnonRateThrottle):
    scope = "create-user"
