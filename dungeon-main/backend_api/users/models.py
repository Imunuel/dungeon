from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from users import constants
from common.models import TimestampedModel, models
from levels.models import Level

User = get_user_model()


class FriendList(models.Model):
    user = models.OneToOneField(User,
                                verbose_name=_("Friend list owner"),
                                related_name="friendlist",
                                on_delete=models.CASCADE)
    friends = models.ManyToManyField("self",
                                     through="Friendships",
                                     symmetrical=True)

    def __str__(self):
        return f"{self.user.username}'s friend list"


class Friendships(TimestampedModel):
    source = models.ForeignKey(FriendList,
                               verbose_name=_("Source user"),
                               related_name="sources",
                               null=True,
                               on_delete=models.SET_NULL)
    target = models.ForeignKey(FriendList,
                               verbose_name=_("Friend with"),
                               related_name="targets",
                               null=True,
                               on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return f"{self.source.user.username} friend with {self.target.user.username}"


class Profile(models.Model):
    """Basic profile entity"""

    user = models.OneToOneField(User,
                                related_name="profile",
                                verbose_name=_("user"),
                                on_delete=models.CASCADE)
    server_location = models.CharField(verbose_name=_("location"),
                                       max_length=2,
                                       choices=constants.SERVER_TYPES)
    level = models.OneToOneField(Level,
                                related_name="profile_level",
                                verbose_name=_("level"),
                                on_delete=models.CASCADE)
    verified = models.BooleanField(default=False)
    last_login = models.DateField(auto_now_add=True)
    login_in_row = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:

        return f"{self.user} in {self.server_location}. {self.level}"
