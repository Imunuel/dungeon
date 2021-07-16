import pytest

from users import services, selectors

pytestmark = [pytest.mark.django_db]


class TestUserSelectors:
    """Testing user selectors"""

    def test_friends_selectors(self, user, another_user, third_user, django_assert_num_queries):
        services.make_friendship(user, another_user, third_user)  # act

        with django_assert_num_queries(2):
            friends = selectors.get_user_friends(user=user)
            friends[0].friends_for
            friends[1].friends_for
