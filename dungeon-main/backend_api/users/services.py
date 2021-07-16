import jwt
import environ

from django.conf import settings
from django.urls import reverse

from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.contrib.sites.shortcuts import get_current_site

from rest_framework_simplejwt.tokens import RefreshToken

env = environ.Env()

from users import validators
from typing import List, Union
import time
from typing import Optional


User = get_user_model()


def user_create(*,
                email: str,
                username: str,
                password: str,
                location: str) -> User:
    """ Service that creates user in database and saving country in profile """

    validators.validate_unique_username(username)

    if User.objects.filter(email=email).exists():
        raise ValidationError("User with this email was already created!")

    user = User(username=username, email=email)
    user.set_password(password)
    user.save()

    validators.validate_correct_location(location)

    user.profile.server_location = location
    user.profile.save()
    return user


def email_verification(request, user: User) -> None:
    """ Service that send message with verification link """

    token = RefreshToken.for_user(user).access_token

    relative_link = reverse('users:email_verify')
    host = env.str('HOST')

    data = f'http://{host}{str(relative_link)}?token={token}'

    subject = 'Verification'
    email_body = f'Hello {user.username}. Use link below to verify your email \n {data}'
    sender = settings.EMAIL_HOST_USER
    receiver = [user.email]

    send_mail(subject, email_body, sender, receiver, fail_silently=False, )


def verify(token: str) -> User:
    """ Service that verify email """
    payload = jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms=['HS256'])
    user = User.objects.get(id=payload['user_id'])
    if not user.profile.verified:
        user.profile.verified = True
        user.profile.save()


def user_update(*, user: User, **update_fields) -> User:
    if update_fields:
        profile_fields = update_fields.pop("profile") if update_fields.get("profile") else None
        if "username" in update_fields:
            username = update_fields.pop('username')
            validators.validate_unique_username(username)
            user.username = username

        if profile_fields:
            if "location" in profile_fields:
                location = profile_fields.pop("location")
                validators.validate_correct_location(location)
                user.profile.server_location = location

        if "first_name" in update_fields:
            first_name = update_fields.pop("first_name")
            user.first_name = first_name

        if "last_name" in update_fields:
            last_name = update_fields.pop("last_name")
            user.last_name = last_name

        user.save()
    return user


def user_update_password(*, user: User, password: str) -> User:
    user.set_password(password)
    user.save()
    return user


def make_friendship(user: User, *friends: Union[User, List[User]]) -> None:
    """Service that establishes friendship between two users"""
    validators.validate_friendship_creation(user, *friends)

    user.friendlist.friends.add(*[friend.friendlist for friend in friends])


def test_service() -> Optional[dict]:
    """ Just a test service for celery task and mock """
    time.sleep(1)
    return {"name": "vladA4paper"}
