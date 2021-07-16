from django.utils.translation import gettext_lazy as _

# Weapon types
SWORD = "SWORD"
HAMMER = "HAMMER"
BOW = "BOW"
DAGGER = "DAGGER"
AXE = "AXE"
CROSSBOW = "CROSSBOW"
LANCE = "LANCE"
RAPIER = "RAPIER"
KNIFE = "KNIFE"
FISTS = "FISTS"

WEAPONS_DICT = {
    SWORD: _("Sword"),
    HAMMER: _("Hammer"),
    BOW: _("Bow"),
    DAGGER: _("Dagger"),
    AXE: _("Axe"),
    CROSSBOW: _("Crossbow"),
    LANCE: _("Lance"),
    RAPIER: _("Rapier"),
    KNIFE: _("Knife"),
    FISTS: _("Fists"),
}


# Buffs
NONE = "NONE"
LIGHTNING = "LIGHTNING"
EARTH = "EARTH"
FLAME = "FLAME"
WIND = "WIND"
WATER = "WATER"
LIGHT = "LIGHT"
DARK = "DARK"

BUFFS_DICT = {
    NONE : _("No buff"),
    LIGHTNING: _("Lightning"),
    EARTH: _("Earth"),
    FLAME: _("Flame"),
    WIND: _("Wind"),
    WATER: _("Water"),
    LIGHT: _("Light"),
    DARK: _("Dark"),
}


WEAPON_TYPES = ((k, v) for k, v in WEAPONS_DICT.items())
BUFF_TYPES = ((k, v) for k, v in BUFFS_DICT.items())
