import pytest

pytestmark = [pytest.mark.django_db]


@pytest.mark.usefixtures('directory', 'media_settings')
class TestFloorMethods:
    """Testing floor model methods e.g. save()"""

    def test_floor_save_method(self, mixer):
        dungeon = mixer.blend("dungeons.Dungeon")
        floor = mixer.blend("floors.Floor", dungeon=dungeon, is_last=True)
        mixer.blend("floors.Floor", dungeon=dungeon, is_last=True)

        floor.refresh_from_db()  # act

        assert not floor.is_last

    def test_floor_different_dungeons(self, mixer):
        dungeon = mixer.blend("dungeons.Dungeon")
        another_dungeon = mixer.blend("dungeons.Dungeon")
        floor = mixer.blend("floors.Floor", dungeon=dungeon, is_last=True)
        mixer.blend("floors.Floor", dungeon=another_dungeon, is_last=True)

        floor.refresh_from_db()  # act

        assert floor.is_last

    def test_floor_saving_queries_num(self, mixer, django_assert_num_queries):  # noqa AAA
        dungeon = mixer.blend("dungeons.Dungeon")
        with django_assert_num_queries(2):
            mixer.blend("floors.Floor", dungeon=dungeon, is_last=True)
