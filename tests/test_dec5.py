import pytest

from advent import dec5


class TestDay5:
    def test_get_data(self):
        data = dec5.get_data()
        assert data[0][0].dest == 50
