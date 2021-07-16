from django.urls import path

from invitations import apis

invitations_patterns = [
    path("create/", apis.UserFriendRequestCreateApi.as_view(), name="create"),
    path("respond/", apis.FriendRequestRespondApi.as_view(), name="respond"),
    path("", apis.FriendRequestsListApi.as_view(), name="list")
]

urlpatterns = invitations_patterns
