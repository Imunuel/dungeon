from unittest.mock import patch

import pytest

from levels.services import (update_exp, get_exp_for_next_level,
                             get_needed_exp_for_next_level)

pytestmark = [pytest.mark.django_db]


class TestLevelServices:
    
    def test_get_exp_for_next_level(self, level):
        exp_for_next_level = get_exp_for_next_level(level=level)
        assert exp_for_next_level == 10

    @pytest.mark.parametrize('number,exp', [
        (1, 5), (2, 10)
    ])
    def test_update_exp(self, level, number, exp):
        new_exp = update_exp(level=level, exp=exp)
        assert new_exp.exp == exp
        assert new_exp.number == number
    
    def test_needed_exp_for_next_level(self, level):
         need_exp = get_needed_exp_for_next_level(level)
         assert need_exp == 10