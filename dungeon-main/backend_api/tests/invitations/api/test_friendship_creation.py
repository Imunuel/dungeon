import pytest
from django.urls import reverse

from invitations.constants import InviteStatus

pytestmark = [pytest.mark.django_db]


class TestFriendshipCreationAPI:
    """Testing friendship creation api, its validation and so on"""

    def test_successful_friend_request_creation(self, api, user, another_user):
        api.force_authenticate(user=another_user)
        url = reverse("users:friends:invites:create", kwargs={"user": user})
        data = {
            "commentary": "I wanna be ur friend!"
        }

        resp = api.post(path=url, data=data, format="json")  # act

        assert resp.status_code == 201
        assert resp.json()["message"] == "Await till user will approve your request."

    def test_friend_request_valid_respond(self, api, user, another_user):
        api.force_authenticate(user=another_user)
        req_url = reverse("users:friends:invites:create", kwargs={"user": user})
        req_data = {
            "commentary": "I wanna be ur friend!"
        }
        api.post(path=req_url, data=req_data, format="json")
        api.logout()
        respond_url = reverse("users:friends:invites:respond", kwargs={"user": user})
        respond_data = {
            "id": user.received_invites.first().id,
            "status": InviteStatus.APPROVED
        }
        api.force_authenticate(user=user)

        resp = api.put(respond_url, respond_data, format="json")  # act

        assert resp.status_code == 200
        assert resp.json()["message"] == "You are now friends with vlad_bumaga!"

    def test_validate_request_for_self(self, api, user):
        api.force_authenticate(user=user)
        url = reverse("users:friends:invites:create", kwargs={"user": user})
        data = {
            "commentary": "I wanna be ur friend!"
        }

        resp = api.post(path=url, data=data, format="json")  # act

        assert resp.status_code == 400
        assert resp.json()["errors"] == ["Can't send friend request to yourself!"]
