import pytest
from django.urls import reverse

pytestmark = [pytest.mark.django_db]


class TestUserCreateThrottle:
    """Testing throttling for user create api"""

    @pytest.mark.slow
    def test_user_throttle_rates(self, api, faker, user_throttle):
        url = reverse("users:create")
        for _ in range(5):
            data = {
                "email": faker.email(),
                "username": faker.name(),
                "password": faker.md5(),
                "location": "AS"
            }
            api.post(path=url, data=data)
        new_data = {
            "email": faker.email(),
            "username": faker.name(),
            "password": faker.md5(),
            "location": "AS"
        }

        resp = api.post(path=url, data=new_data)  # act

        assert resp.status_code == 429
