import pytest
from django.urls import reverse

from tests import factories

pytestmark = [pytest.mark.django_db]


class TestDungeonApi:

    def test_dungeon_detail(self, api, user):
        api.force_authenticate(user=user)
        path = factories.PathFactory()
        dungeon = factories.DungeonFactory(path=path)
        url = reverse('dungeon_detail', kwargs={"pk": dungeon.pk})

        response = api.get(url)  # act

        assert response.status_code == 200
