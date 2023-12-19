from math import lcm

import pytest

from advent import dec8


class TestDay:
    def test_get_data(self):
        data = dec8.get_data()
        assert data["BBB"][0] == "AAA"

    def test_get_answer(self):
        result = dec8.get_answer()
        assert result == 6

    @pytest.mark.skip
    def test_get_real_answer(self):
        result = dec8.get_answer(toy=False)
        assert result == 0

    def test_get_ghost_answer(self):
        result = dec8.get_ghost_answer(toy=True, ghost=True)
        assert result == 6

    @pytest.mark.skip("really slow")
    def test_get_real_ghost_answer(self):
        result = dec8.get_ghost_answer(toy=False)
        assert result == 6

    @pytest.mark.skip
    def test_get_better_ghost_answer(self):
        result = dec8.get_efficient_ghost_answer(toy=False)
        assert result == 0
