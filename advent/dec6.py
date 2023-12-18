import csv
from functools import reduce

from pydantic import BaseModel


class RaceMemo(BaseModel):
    time: int
    distance: int

    def is_winning_number(self, pre: int) -> bool:
        return pre * (self.time - pre) > self.distance

    def ways_to_win(self) -> int:
        results = [pre * (self.time - pre) for pre in range(1, self.time)]
        return sum(x > self.distance for x in results)


a = [1, 2, 3]
reduce(lambda x, y: x * y, a, 1)


def get_data(day: int = 6, toy: bool = True) -> list[RaceMemo]:
    filename = f"{'toy' if toy else ''}data/dec{int(day)}.csv"
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        rows = []
        for row in csv_reader:
            rows.append(RaceMemo(time=row[0], distance=row[1]))
    return rows


def get_answer(day: int = 6, toy: bool = True) -> int:
    data = get_data(day=day, toy=toy)
    wins = [x.ways_to_win() for x in data]
    return reduce(lambda x, y: x * y, wins, 1)
