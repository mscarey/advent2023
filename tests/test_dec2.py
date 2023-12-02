from advent import dec2


class TestToy:
    def test_get_answer(self):
        assert dec2.get_answer(day=2) == 8

    def test_get_final_answer(self):
        assert dec2.get_final_answer(day=2) == 2286


class TestReal:
    def test_get_answer(self):
        assert dec2.get_answer(day=2, toy=False) == 2545

    def test_get_final_answer(self):
        assert dec2.get_final_answer(day=2, toy=False) == 78111
