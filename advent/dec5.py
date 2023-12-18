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


def get_seeds(day: int = 5, toy: bool = True) -> list[int]:
    filename = f"{'toy' if toy else ''}data/dec{int(day)}_seeds.csv"
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=" ")
        row = next(csv_reader)
        return [int(x) for x in row]


def get_next_value(seed: int, phase: list[RangeMemo]) -> int:
    for memo in phase:
        if memo.source <= seed < memo.source + memo.length:
            return memo.dest + (seed - memo.source)
    return seed


def get_location(seed: int, phases: list[list[RangeMemo]]) -> int:
    for phase in phases:
        seed = get_next_value(seed, phase)
    return seed


def get_answer(day: int = 5, toy: bool = True) -> int:
    phases = get_data(day=day, toy=toy)
    seeds = get_seeds(day=day, toy=toy)
    return min([get_location(seed=seed, phases=phases) for seed in seeds])


def get_prior_step(location: int, phase: list[RangeMemo]) -> int:
    for memo in phase:
        if memo.dest <= location < memo.dest + memo.length:
            return memo.source + (location - memo.dest)
    return location


def get_seed_from_location(location: int, phases: list[list[RangeMemo]]) -> int:
    for phase in phases[::-1]:
        location = get_prior_step(location, phase=phase)
    return location


def get_seed_for_lowest_location(day: int = 5, toy: bool = True) -> int:
    phases = get_data(day=day, toy=toy)
    seeds = get_seeds(day=day, toy=toy)
    seed_ranges = list(zip(seeds[::2], seeds[1::2]))
    for location in range(1, 10000000):
        seed = get_seed_from_location(location=location, phases=phases)
        for x, y in seed_ranges:
            if x <= seed < (x + y):
                return location
    return -1
