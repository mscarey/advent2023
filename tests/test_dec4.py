import pytest

from advent import dec4


class TestDay4:
    def test_get_data(self):
        data = dec4.get_data()
        assert data[0].wanted[0] == 41

    def test_get_score(self):
        score = dec4.get_score(day=4, toy=True)
        assert score == 13

    def test_get_real_score(self):
        score = dec4.get_score(day=4, toy=False)
        assert score == 20107

    def test_count_up_cards(self):
        score = dec4.count_up_cards(day=4, toy=True)
        assert score == 30

    @pytest.mark.skip(reason="slow")
    def test_count_up_cards_real(self):
        score = dec4.count_up_cards(day=4, toy=False)
        assert score == 8172507
