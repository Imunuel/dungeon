import shutil

import pytest
from mixer.backend.django import mixer as _mixer
from rest_framework.test import APIClient, APIRequestFactory
from pytest_factoryboy import register
from tests import factories

pytestmark = [pytest.mark.django_db]

register(factories.TokenFactory, "token")

TEST_MEDIA_ROOT = "/tmp/pytest-of-root/pytest-0/test_media0"


@pytest.fixture
def mixer():
    return _mixer


@pytest.fixture
def api():
    return APIClient()


@pytest.fixture
def get_data(mocker):
    return mocker.patch('users.tasks.services.test_service')


@pytest.fixture
def user(mixer):
    return mixer.blend("auth.User", username="deepdarkfantasy")


@pytest.fixture
def another_user():
    return factories.UserFactory(username="vlad_bumaga",
                                 password="VsemPrivetSVamiVladA4")


@pytest.fixture
def third_user():
    return factories.UserFactory(username="swallow_marlow")


@pytest.fixture
def invite(user, another_user):
    return factories.InvitationFactory(
        sender=another_user,
        invitee=user,
        status=1
    )


@pytest.fixture
def another_invite(user, third_user):
    return factories.InvitationFactory(
        sender=third_user,
        invitee=user,
        status=1
    )


@pytest.fixture
def user_throttle(mocker):
    return mocker.patch('users.apis.CreateUserRateThrottle')


@pytest.fixture(scope='module')
def directory(tmpdir_factory):
    my_tmpdir = tmpdir_factory.mktemp("test_media")
    yield my_tmpdir
    shutil.rmtree(str(my_tmpdir))


@pytest.fixture(scope="function")
def media_settings(settings):
    settings.MEDIA_ROOT = TEST_MEDIA_ROOT


@pytest.fixture
def level():
    return factories.LevelFactory()


@pytest.fixture
def rf():
    return APIRequestFactory()