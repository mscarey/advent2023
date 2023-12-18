import pytest

from advent import dec5


class TestDay5:
    def test_get_data(self):
        data = dec5.get_data()
        assert data[0][0].dest == 50

    def test_get_seeds(self):
        seeds = dec5.get_seeds()
        assert seeds == [79, 14, 55, 13]

    def test_get_answer(self):
        answer = dec5.get_answer()
        assert answer == 35

    def test_get_real_answer(self):
        """
        Tried 553461990.

        That's not the right answer; your answer is too low.
        """
        answer = dec5.get_answer(toy=False)
        assert answer == 553461990

    def test_get_seed_for_lowest_location(self):
        answer = dec5.get_seed_for_lowest_location()
        assert answer == 46

    @pytest.mark.skip
    def test_get_seed_for_real_lowest_location(self):
        """
        Tried 0. Seemed to be within a covered range on the first try.

        That's not the right answer.
        """
        answer = dec5.get_seed_for_lowest_location(toy=False)
        assert answer == 46
