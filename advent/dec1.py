import csv
import re


def get_data(day: int = 1, toy: bool = True) -> list[str]:
    filename = f"data/{'toy' if toy else 'dec'}{int(day)}.csv"
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        answers = []
        for row in csv_reader:
            answers.append(row[0])
    return answers


def get_word_value(code: str) -> int:
    digits = re.findall(r"\d", code)
    number = f"{digits[0]}{digits[-1]}"
    return int(number)


def word_to_digit(word: str) -> str:
    return (
        word.replace("one", "1")
        .replace("two", "2")
        .replace("three", "3")
        .replace("four", "4")
        .replace("five", "5")
        .replace("six", "6")
        .replace("seven", "7")
        .replace("eight", "8")
        .replace("nine", "9")
    )


def get_wordy_word_value(code: str) -> int:
    digits = re.findall(r"(\d|zero|one|two|three|four|five|six|seven|eight|nine)", code)
    first = word_to_digit(digits[0])
    last = word_to_digit(digits[-1])
    number = f"{first}{last}"
    return int(number)


def get_answer(day: int = 1, toy: bool = True) -> int:
    data = get_data(day=day, toy=toy)
    return sum([get_word_value(word) for word in data])


def get_final_answer(day: int = 1, toy: bool = True) -> int:
    """This got 54533; too high."""
    data = get_data(day=day, toy=toy)
    return sum([get_wordy_word_value(word) for word in data])
