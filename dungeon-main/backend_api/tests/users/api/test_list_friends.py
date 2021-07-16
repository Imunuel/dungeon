import pytest
from django.urls import reverse

from users import services

pytestmark = [pytest.mark.django_db]


class TestFriendList:
    """
    Testing friend list api for getting friends.
    Using pytest-freezegun to test dates.
    """

    @pytest.mark.freeze_time('2021-06-10')
    def test_two_friends_list(self,
                              api,
                              freezer,
                              user,
                              another_user,
                              third_user):
        url = reverse("users:friends:list", kwargs={"user": user})
        services.make_friendship(user, another_user, third_user)
        freezer.move_to("2021-06-15")

        resp = api.get(url)  # act

        assert resp.status_code == 200
        assert "swallow_marlow" in [friend["username"] for friend in resp.json()]
        assert resp.json()[0]["friends_for"] == "5 days"
