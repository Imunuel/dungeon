from django.urls import path, include, register_converter

from users import apis
from invitations import urls as invitations_urls
from users.converters import UserConverter

register_converter(UserConverter, 'user')

friends_patterns = [
    path(r'', apis.UserFriendsListApi.as_view(), name="list"),
    path(r'invites/', include((invitations_urls, "invites")))
]

user_patterns = [
    path('create/', apis.UserCreateApi.as_view(), name="create"),
    path('<user:user>/update/', apis.UserUpdateApi.as_view(), name="update"),
    path('<user:user>/set_password', apis.UserUpdatePasswordApi.as_view(), name="set_password"),
    path('<user:user>/friends/', include((friends_patterns, "friends"))),
    path('<user:user>', apis.UserDetailApi.as_view(), name="detail"),
    path('email_verify/', apis.VerifyEmail.as_view(), name="email_verify"),
]

urlpatterns = user_patterns
