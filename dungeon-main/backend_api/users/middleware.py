from datetime import timedelta as td, datetime

from django.utils import timezone
from django.db.models.expressions import F

from config.settings import LAST_ACTIVITY_INTERVAL
from users.models import Profile
from users.constants import MAXIMUM_DAY


def last_user_activity_middleware(get_response):

    def middleware(request):

        response = get_response(request)

        expected_entry_date = datetime.today().date() - td(seconds=LAST_ACTIVITY_INTERVAL)

        if request.user.is_authenticated and request.user.profile.last_login == expected_entry_date:
            Profile.objects.filter(pk=request.user.pk).update(last_login=timezone.now(), login_in_row=F('login_in_row') + 1)
            request.user.refresh_from_db()
            if request.user.profile.login_in_row == MAXIMUM_DAY:
                request.user.profile.login_in_row = 0
                request.user.refresh_from_db()
        elif request.user.is_authenticated and request.user.profile.last_login < expected_entry_date:
            request.user.profile.login_in_row = 0
            request.user.refresh_from_db()

        return response

    return middleware
