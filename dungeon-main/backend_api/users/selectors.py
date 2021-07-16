from django.utils import timezone
from django.db.models import F, QuerySet, DateTimeField, ExpressionWrapper

from django.contrib.auth import get_user_model

User = get_user_model()


def get_user_friends(*, user: User) -> QuerySet[User]:
    expression = ExpressionWrapper(timezone.now() - F("friendlist__sources__created"),
                                   output_field=DateTimeField())
    queryset = User.objects \
        .filter(friendlist__friends__user_id=user.pk) \
        .annotate(friends_for=expression) \
        .order_by("-friendlist__sources__created")
    return queryset


def get_user_detail(*, user: User) -> QuerySet[User]:
    queryset = User.objects.get(pk=user.pk)
    return queryset
