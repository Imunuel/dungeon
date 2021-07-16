from typing import List

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from users import constants

User = get_user_model()


def validate_unique_username(username: str) -> None:
    if User.objects.filter(username=username).exists():
        raise ValidationError("User with this username was already created!")


def validate_correct_location(location: str) -> None:
    if location not in constants.SERVERS_DICT.keys():
        raise ValidationError("Unexpected location type!")


def validate_friendship_creation(user: User, *friends: List[User]) -> None:
    if user in friends:
        raise ValidationError("You can't be friend with yourself!")
