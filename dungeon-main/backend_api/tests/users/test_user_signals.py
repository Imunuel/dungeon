import pytest
from rest_framework.authtoken.models import Token

pytestmark = [pytest.mark.django_db]


class TestUserSignals:
    """Testing signals associated with users and relate tables"""

    def test_relational_fields_creation(self, mixer):
        with mixer.ctx(commit=False):
            user = mixer.blend('auth.User', username="deep-dark-fantasy")

        user.save()  # act
        token = Token.objects.get(user=user)
        
        assert token is not None
        assert user.profile is not None
        assert user.profile.level is not None
