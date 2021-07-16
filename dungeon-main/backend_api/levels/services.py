from django.db.models import F
from django.contrib.auth import get_user_model

from levels.models import Level

User = get_user_model()


def check_exp_for_next_level(level: Level) -> bool:
    """checks if the level can be updated"""

    return not level.exp < get_exp_for_next_level(level)


def get_exp_for_next_level(level: Level) -> int:
    """get expierence for the next level"""

    current_exp = 10 #necessary experience for Level 2
    for l in range(level.number): #level.number is the current number level
        current_exp += 10 * l #upgrade current exp
    return current_exp


def set_next_level(level: Level) -> Level:
    """set the next level"""

    if check_exp_for_next_level(level):
        Level.objects.filter(pk=level.pk).update(number=F('number') + 1)
        level.refresh_from_db()
        return level
        

def update_exp(level: Level, exp: int) -> Level:
    """"update your experience and check the level up"""

    Level.objects.filter(pk=level.pk).update(exp=F('exp') + exp)
    level.refresh_from_db()
    set_next_level(level)
    return level


def get_needed_exp_for_next_level(level: Level) -> int:
    """get needed exp for level up"""

    current_exp = level.exp
    needed_exp = get_exp_for_next_level(level) - current_exp
    return needed_exp