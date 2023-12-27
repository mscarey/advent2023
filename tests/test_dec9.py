import pytest

from advent import dec9


class TestDay:
    def test_get_data(self):
        data = dec9.get_data()
        assert data[0] == [0, 3, 6, 9, 12, 15]

    @pytest.mark.parametrize(
        "data,expected",
        [
            ([0, 3, 6, 9, 12, 15], 18),
            ([1, 3, 6, 10, 15, 21], 28),
            ([10, 13, 16, 21, 30, 45], 68),
        ],
    )
    def test_get_next_value(self, data, expected):
        assert dec9.get_next_value(data) == expected

    def test_get_answer(self):
        assert dec9.get_answer() == 114

    @pytest.mark.skip
    def test_get_real_answer(self):
        assert dec9.get_answer(toy=False) == 0

    @pytest.mark.parametrize(
        "data,expected",
        [
            ([0, 3, 6, 9, 12, 15], -3),
            ([1, 3, 6, 10, 15, 21], 0),
            ([10, 13, 16, 21, 30, 45], 5),
        ],
    )
    def test_get_prior_value(self, data, expected):
        assert dec9.get_prior_value(data) == expected

    def test_get_prior_answer(self):
        assert dec9.get_prior_answer() == 2

    @pytest.mark.skip
    def test_get_real_prior_answer(self):
        assert dec9.get_prior_answer(toy=False) == 2
