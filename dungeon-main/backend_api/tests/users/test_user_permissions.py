import pytest
from mock import Mock

from tests import factories
from users import permissions


pytestmark = [pytest.mark.django_db]


class TestObjectOwnerPerm:

    def test_valid_user_for_permission(self, rf):
        user_1 = factories.UserFactory()
        view = Mock()
        view.kwargs = {'user': user_1}
        request = Mock()
        request.user = user_1
        my_permission = permissions.IsObjectOwner()
        perm = my_permission.has_permission(request, view)

        assert perm is True