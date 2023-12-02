from advent import dec1
import pytest


class TestToy:
    @pytest.mark.parametrize(
        "code,result",
        [
            ("1abc2", 12),
            ("pqr3stu8vwx", 38),
            ("a1b2c3d4e5f", 15),
            ("treb7uchet", 77),
        ],
    )
    def test_trebuchet(self, code, result):
        assert dec1.get_word_value(code) == result

    def test_get_answer(self):
        assert dec1.get_answer() == 142

    @pytest.mark.parametrize(
        "code,result",
        [
            ("two1nine", 29),
            ("eightwothree", 83),
            ("abcone2threexyz", 13),
            ("xtwone3four", 24),
            ("4nineeightseven2", 42),
            ("zoneight234", 14),
            ("7pqrstsixteen", 76),
        ],
    )
    def test_wordy_trebuchet(self, code, result):
        assert dec1.get_wordy_word_value(code) == result


class TestReal:
    def test_get_answer(self):
        assert dec1.get_answer(toy=False) == 54331

    def test_get_final_answer(self):
        assert dec1.get_final_answer(toy=False) == 54533
