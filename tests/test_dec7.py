import pytest

from advent import dec7


class TestDay:
    def test_get_data(self):
        data = dec7.get_data()
        assert data[0].hand == "32B3E"

    def test_get_kind(self):
        data = dec7.get_data()
        assert data[0].kind == "21"
        assert data[1].kind == "31"
        assert data[2].kind == "22"
        assert data[3].kind == "22"
        assert data[4].kind == "31"
        assert dec7.CardMemo(hand="AAAAA", bid=1).kind == "5"

    def test_sort_cards(self):
        data = dec7.get_data()
        result = sorted(data)
        assert result[0].hand == "32B3E"
        assert result[4].hand == "DDDCF"

    def test_get_answer(self):
        result = dec7.get_answer()
        assert result == 6440

    @pytest.mark.skip
    def test_get_real_answer(self):
        result = dec7.get_answer(toy=False)
        assert result == 0
