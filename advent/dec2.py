import csv


def get_data(day: int = 1, toy: bool = True) -> list[list[str]]:
    filename = f"{'toy' if toy else ''}data/dec{int(day)}.csv"
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        answers = []
        for row in csv_reader:
            answers.append(row)
    return answers


def item_is_possible(item: str) -> bool:
    number, color = item.split()
    match color:
        case "red":
            return int(number) <= 12
        case "green":
            return int(number) <= 13
        case "blue":
            return int(number) <= 14
    raise ValueError(f"color is {color}")


def row_is_possible(row: list[str]) -> bool:
    for item in row:
        if not item_is_possible(item):
            return False
    return True


def get_answer(day: int = 2, toy: bool = True) -> int:
    data = get_data(day=day, toy=toy)
    score = 0
    for index, row in enumerate(data):
        if row_is_possible(row):
            score += index + 1
    return score


def get_cubed_score(row: list[str]) -> int:
    cubes = {"red": 0, "green": 0, "blue": 0}
    for item in row:
        number, color = item.split()
        cubes[color] = max(int(number), cubes[color])
    return cubes["red"] * cubes["green"] * cubes["blue"]


def get_final_answer(day: int = 2, toy: bool = True) -> int:
    data = get_data(day=day, toy=toy)
    return sum([get_cubed_score(row) for row in data])
