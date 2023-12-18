from functools import reduce

from advent import dec6


class TestDay5:
    def test_get_data(self):
        data = dec6.get_data()
        assert data[0].distance == 9

    def test_count_ways_to_win(self):
        memo = dec6.RaceMemo(time=7, distance=9)
        assert memo.ways_to_win() == 4

    def test_get_answer(self):
        result = dec6.get_answer()
        assert result == 288

    def test_get_real_answer(self):
        result = dec6.get_answer(toy=False)
        assert result == 316800

    def test_get_long_race_answer(self):
        memo = dec6.RaceMemo(time=71530, distance=940200)
        assert memo.ways_to_win() == 71503

    def test_get_real_long_race_answer(self):
        memo = dec6.RaceMemo(time=61677571, distance=430103613071150)
        assert not memo.is_winning_number(8014958)
        assert memo.is_winning_number(8014959)
        assert memo.is_winning_number(53662612)
        assert not memo.is_winning_number(53662613)
        assert 53662613 - 8014959 == 45647654
