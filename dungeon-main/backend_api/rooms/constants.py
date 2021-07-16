from django.utils.translation import gettext_lazy as _

DEFAULT_ROOM = "DEFAULT_ROOM"
MONSTER_ROOM = "MONSTER_ROOM"


ROOMS_DICT = {
    DEFAULT_ROOM: _("Default room"),
    MONSTER_ROOM: _("Room with monster"),
}


ROOMS_TYPES = ((k, v) for k, v in ROOMS_DICT.items())
