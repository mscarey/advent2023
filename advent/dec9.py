import csv


def get_data(day: int = 9, toy: bool = True) -> list[list[int]]:
    filename = f"{'toy' if toy else ''}data/dec{int(day)}.csv"
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=" ")
        rows = []
        for row in csv_reader:
            rows.append([int(x) for x in row])
    return rows


def get_next_value(data: list[int]) -> int:
    differences = [x - data[i] for i, x in enumerate(data[1:])]
    if all(x == 0 for x in differences):
        return data[-1]
    return data[-1] + get_next_value(differences)


def get_answer(day: int = 9, toy: bool = True) -> int:
    data = get_data(day=day, toy=toy)
    return sum(get_next_value(row) for row in data)


def get_prior_value(data: list[int]) -> int:
    differences = [x - data[i] for i, x in enumerate(data[1:])]
    if all(x == 0 for x in differences):
        return data[0]
    return data[0] - get_prior_value(differences)


def get_prior_answer(day: int = 9, toy: bool = True) -> int:
    data = get_data(day=day, toy=toy)
    return sum(get_prior_value(row) for row in data)
