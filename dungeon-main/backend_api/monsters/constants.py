from django.utils.translation import gettext_lazy as _

ATTACK = "ATK"
STATIC = "STTC"
DAMAGED = "DMGD"
DEAD = "DD"

SPRITES_DICT = {
    ATTACK: _("attack"),
    STATIC: _("static"),
    DAMAGED: _("damaged"),
    DEAD: _("dead"),
}


SPRITE_TYPES = ((k, v) for k, v in SPRITES_DICT.items())
