from datetime import timedelta

from mock import Mock
import pytest
from django.contrib.auth import get_user_model

from tests import factories
from users import middleware


User = get_user_model()
pytestmark = [pytest.mark.django_db]


class TestUserLastActivityMiddleware:

    def test_middleware(self, rf):
        user = factories.UserFactory()
        request = rf.post("/")
        request.user = user
        request.user.profile.last_login -= timedelta(seconds=86400)
        my_middleware = middleware.last_user_activity_middleware(Mock())
        my_middleware(request)

        assert user.profile.login_in_row == 1

    def test_middleware_unexpected_entry_date(self, rf):
        user = factories.UserFactory()
        request = rf.post("/")
        user.profile.login_in_row = 2
        request.user = user
        request.user.profile.last_login -= timedelta(seconds=86400 * 2)
        my_middleware = middleware.last_user_activity_middleware(Mock())
        my_middleware(request)

        assert user.profile.login_in_row == 0
