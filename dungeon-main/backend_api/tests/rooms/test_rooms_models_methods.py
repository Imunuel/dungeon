import pytest

pytestmark = [pytest.mark.django_db]


@pytest.mark.usefixtures('directory', 'media_settings')
class TestRoomMethods:
    """Testing room model methods e.g. save()"""

    def test_room_save_method(self, mixer):
        floor = mixer.blend("floors.Floor")
        room = mixer.blend("rooms.Room", is_last=True, floor=floor)
        mixer.blend("rooms.Room", is_last=True, floor=floor)

        room.refresh_from_db()  # act

        assert not room.is_last

    def test_room_different_floors(self, mixer):
        floor = mixer.blend("floors.Floor")
        another_floor = mixer.blend("floors.Floor")
        room = mixer.blend("rooms.Room", is_last=True, floor=floor)
        mixer.blend("rooms.Room", is_last=True, floor=another_floor)

        room.refresh_from_db()  # act

        assert room.is_last

    def test_room_saving_queries_num(self, mixer, django_assert_num_queries):  # noqa AAA
        floor = mixer.blend("floors.Floor")
        with django_assert_num_queries(2):
            mixer.blend("rooms.Room", floor=floor, is_last=True)
