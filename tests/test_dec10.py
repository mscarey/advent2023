import pytest

from advent import dec1
from advent import dec10


class TestDay:
    def test_get_data(self):
        data = dec1.get_data(day=10)
        assert data[0] == "..F7."
        assert dec10.find_s(data) == (0, 2)

    def test_get_pipe_postitions(self):
        data = dec10.get_pipe_positions()
        assert data[0] == "..F7."
        assert dec10.find_s(data) == (0, 2)

    def test_get_answer(self):
        assert dec10.get_answer() == 8

    @pytest.mark.skip
    def test_get_real_answer(self):
        assert dec10.get_answer(toy=False) == 8
