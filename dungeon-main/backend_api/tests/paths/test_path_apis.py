import pytest
from django.urls import reverse
from django.test import override_settings

from tests import factories


pytestmark = [pytest.mark.django_db]


class TestPathApi:
    TEST_MEDIA_ROOT = "/tmp/pytest-of-root/pytest-0/test_media0"

    def test_list_api(self, api, user):
        api.force_authenticate(user=user)
        factories.PathFactory()
        factories.PathFactory()
        url = reverse('path_list')

        response = api.get(url)  # act

        assert response.status_code == 200
        assert len(response.json()) == 2

    @override_settings(MEDIA_ROOT=TEST_MEDIA_ROOT)
    def test_path_detail(self, api, directory, user):
        api.force_authenticate(user=user)
        path_1 = factories.PathFactory()
        texture_1 = factories.TextureFactory()
        dungeon_1 = factories.DungeonFactory(path=path_1)
        url = reverse('path_detail', kwargs={'path': path_1})
        path_1.textures.add(texture_1)

        response = api.get(url)  # act

        assert response.status_code == 200
        assert len(response.data['textures']) == 1
        assert len(response.data['dungeons']) == 1
        assert response.data['textures'][0]['id'] == texture_1.id
        assert response.data['dungeons'][0]['id'] == dungeon_1.id
