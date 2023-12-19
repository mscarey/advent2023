import csv
from itertools import cycle


def get_data(day: int = 8, toy: bool = True) -> dict[str, tuple[str, str]]:
    filename = f"{'toy' if toy else ''}data/dec{int(day)}.csv"
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        result = {}
        for row in csv_reader:
            result[row[0]] = (row[1], row[2])
    return result


def get_steps(day: int = 8, toy: bool = True) -> str:
    filename = f"{'toy' if toy else ''}data/dec{int(day)}_steps.txt"
    with open(filename) as csv_file:
        rows = csv_file.readlines()
        return str(rows[0])


def get_answer(day: int = 8, toy: bool = True) -> int:
    location = "AAA"
    steps = cycle(get_steps(day=day, toy=toy))
    nodes = get_data(day=day, toy=toy)
    for i, step in enumerate(steps):
        if step == "L":
            location = nodes[location][0]
        else:
            location = nodes[location][1]
        if location == "ZZZ":
            return i + 1
    return -1
