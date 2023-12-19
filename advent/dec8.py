import csv
from collections import defaultdict
from itertools import cycle
from math import lcm

from pydantic import BaseModel


def get_data(
    day: int = 8, toy: bool = True, ghost: bool = False
) -> dict[str, tuple[str, str]]:
    filename = f"{'toy' if toy else ''}data/dec{int(day)}{'ghost' if ghost else ''}.csv"
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


def get_ghost_answer(day: int = 8, toy: bool = True, ghost: bool = False) -> int:
    """Calculate answer only fast enough for the test data, not the real data."""
    nodes = get_data(day=day, toy=toy, ghost=ghost)
    locations = [x for x in nodes if x.endswith("A")]
    if ghost:
        steps = cycle("LR")
    else:
        steps = cycle(get_steps(day=day, toy=toy))
    for i, step in enumerate(steps):
        if step == "L":
            locations = [nodes[location][0] for location in locations]
        else:
            locations = [nodes[location][1] for location in locations]
        if all([x.endswith("Z") for x in locations]):
            return i + 1
    return -1


class WanderingMemo(BaseModel):
    wanderings: dict[str, dict[int, int]]
    cycle_length: int


def get_wanderings(
    location: str, steps: str, nodes: dict[str, tuple[str, str]]
) -> WanderingMemo:
    all_steps = 0
    wanderings: dict[str, dict[int, int]] = defaultdict(dict)
    while True:
        for i, step in enumerate(steps):
            if step == "L":
                location = nodes[location][0]
            else:
                location = nodes[location][1]
            if location.endswith("Z"):
                if wanderings[location].get(i) is not None:
                    cycle_length = all_steps + i - wanderings[location][i]
                    return WanderingMemo(
                        wanderings=wanderings, cycle_length=cycle_length
                    )
                wanderings[location][i] = all_steps + i
        all_steps += len(steps)


def get_efficient_ghost_answer(day: int = 8, toy: bool = True) -> int:
    nodes = get_data(day=day, toy=toy)
    steps = get_steps(day=day, toy=toy)
    ghosts = [x for x in nodes if x.endswith("A")]
    all_wanderings = [
        get_wanderings(location=ghost, steps=steps, nodes=nodes) for ghost in ghosts
    ]
    convergence = lcm(*[x.cycle_length for x in all_wanderings])

    return convergence
