from django.utils.translation import gettext_lazy as _


class InviteStatus:
    PENDING = 1
    APPROVED = 2
    DECLINED = 3

    DICT = {
        PENDING: _("pending"),
        APPROVED: _("approved"),
        DECLINED: _("declined")
    }

    CHOICES = ((k, v) for k, v in DICT.items())

    RESPONDS = [APPROVED, DECLINED]

    RESPOND_MESSAGES = {
        APPROVED: "You are now friends with {}!",
        DECLINED: "You've decided to decline {} friend request!"
    }


REQUEST_REPLY_MESSAGE = "Await till user will approve your request."
