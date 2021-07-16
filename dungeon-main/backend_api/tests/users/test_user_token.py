import pytest

from rest_framework.authtoken.models import Token

from tests import factories

pytestmark = [pytest.mark.django_db]


class TestToken:

    def test_create_token(self):
        user = factories.UserFactory()
        token = Token.objects.get(user=user)

        assert token.key is not None
    
