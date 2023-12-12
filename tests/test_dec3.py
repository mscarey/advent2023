from advent import dec3


class TestDec3:
    def test_get_data(self):
        result = dec3.get_data(toy=True, day=3)
        assert result[1] == "467..114.."

    def test_get_score(self):
        result = dec3.get_score(toy=True, day=3)
        assert result == 4361

    def test_get_real_score(self):
        result = dec3.get_score(toy=False, day=3)
        assert result == 517021

    def test_get_gear_ratio_sum(self):
        result = dec3.get_gear_ratio_sum(day=3, toy=True)
        assert result == 467835

    def test_get_real_gear_ratio_sum(self):
        result = dec3.get_gear_ratio_sum(day=3, toy=False)
        assert result == 81296995
