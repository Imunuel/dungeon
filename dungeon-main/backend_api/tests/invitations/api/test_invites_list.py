from datetime import datetime

import pytest
from django.urls import reverse

pytestmark = [pytest.mark.django_db]


class TestInvitesList:
    """Testing list api for invites"""

    def test_list_api_list_invites(self,  # noqa AAA
                                   api,
                                   freezer,
                                   user,
                                   third_user,
                                   invite,
                                   another_invite,
                                   django_assert_num_queries):
        url = reverse("users:friends:invites:list", kwargs={"user": user})

        resp = api.get(url)  # act

        assert resp.status_code == 200
        assert len(resp.json()) == 2
        assert resp.json()[0]["sent_at"] == datetime.now().strftime("%B %d, %Y")
        assert resp.json()[1]["sender"]["username"] == third_user.username

    def test_invites_list_api_queries_num(self,  # noqa AAA
                                          api,
                                          user,
                                          invite,
                                          django_assert_num_queries):
        url = reverse("users:friends:invites:list", kwargs={"user": user})

        with django_assert_num_queries(2):
            api.get(url)
