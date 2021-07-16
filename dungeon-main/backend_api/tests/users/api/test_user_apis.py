import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model

from tests import factories

User = get_user_model()
pytestmark = [pytest.mark.django_db]


class TestUserCreateApi:
    """ Testing user creation api """

    def test_user_creation(self, api):
        url = reverse("users:create")
        data = {
            "email": "popit@tut.by",
            "username": "simpledimple",
            "password": "popitcooler123456",
            "location": "NA"
        }

        resp = api.post(path=url, data=data, format="json")  # act

        assert resp.status_code == 201

    def test_user_validation_unique_name(self, api, mixer, user):
        api.force_authenticate(user=user)
        url = reverse("users:create")
        data = {
            "email": "test@tut.by",
            "username": "test",
            "password": "test123",
            "location": "NA"
        }
        mixer.blend("auth.User", username="test", password="test123")

        resp = api.post(path=url, data=data, format="json")  # act

        assert resp.status_code == 400
        assert resp.json()["errors"] == ["User with this username was already created!"]

    def test_user_validation_location(self, api):
        data = {
            "email": "test@tut.by",
            "username": "test",
            "password": "test123",
            "location": "PY"
        }
        url = reverse("users:create")

        resp = api.post(path=url, data=data, format="json")  # act

        assert resp.status_code == 400
        assert resp.json()['errors'] == ["Unexpected location type!"]


class TestUserUpdateApi:

    def test_user_update(self, api, mixer):  # noqa AAA
        user = mixer.blend("auth.User")
        api.force_authenticate(user=user)
        data = {
            "email": "popit@tut.by",
            "username": "simpledimple",
            "first_name": "ddadada",
            "last_name": "popit",
            "profile": {
                "location": "EU"
            }
        }
        url = reverse("users:update", kwargs={'user': user})

        response = api.post(path=url, data=data, format="json")
        user.refresh_from_db()

        assert response.status_code == 200
        assert user.first_name == data["first_name"]
        assert user.username == data["username"]

    def test_user_update_validation_username(self, api):
        data = {
            "username": "deepdarkfantasy"
        }
        user = factories.UserFactory()
        api.force_authenticate(user=user)
        url = reverse("users:update", kwargs={'user': user})

        response = api.post(path=url, data=data, format="json")  # act

        assert response.status_code == 400
        assert response.json()["errors"] == ["User with this username was already created!"]

    def test_user_update_validation_location(self, api):
        data = {
            "profile": {
                "location": "PY"
            }
        }
        user = factories.UserFactory()
        api.force_authenticate(user=user)
        url = reverse("users:update", kwargs={'user': user})

        response = api.post(path=url, data=data, format="json")  # act

        assert response.status_code == 400
        assert response.json()['errors'] == ["Unexpected location type!"]


class TestUserResetPassword:

    def test_user_reset_password(self, api):  # noqa AAA
        data = {
            "password": "lambda123"
        }
        user = factories.UserFactory()
        api.force_authenticate(user=user)
        url = reverse("users:set_password", kwargs={'user': user})

        response = api.post(path=url, data=data, format="json")
        user.refresh_from_db()

        assert response.status_code == 200
        assert user.check_password(data["password"])


class TestUserDetailApi:

    def test_user_detail(self, api):
        user = factories.UserFactory()
        api.force_authenticate(user)
        url = reverse('users:detail', kwargs={'user': user})

        response = api.get(path=url, format="json")

        assert response.status_code == 200
        assert user.username == response.data["username"]
