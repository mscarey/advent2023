import csv

from pydantic import BaseModel


class RangeMemo(BaseModel):
    dest: int
    source: int
    length: int


def get_data(day: int = 5, toy: bool = True) -> list[list[RangeMemo]]:
    filename = f"{'toy' if toy else ''}data/dec{int(day)}.csv"
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=" ")
        rows = []
        for row in csv_reader:
            rows.append([int(x) for x in row])
    phases: list[list[RangeMemo]] = [[] for x in range(7)]
    for row in rows:
        phases[row[0]].append(RangeMemo(dest=row[1], source=row[2], length=row[3]))
    return phases
