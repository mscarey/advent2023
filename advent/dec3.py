from collections import defaultdict
from typing import NamedTuple

import re

from advent.dec1 import get_data


def get_score(day: int = 3, toy: bool = False):
    """
    Get total value of component numbers.

    519225 was too high.
    """
    schematic = get_data(day=day, toy=toy)
    score = 0
    for rownum, row in enumerate(schematic):
        matches = re.finditer(r"\d+", row)
        for match in matches:
            is_part_number = False
            for y in range(rownum - 1, rownum + 2):
                for x in range(match.start() - 1, match.end() + 1):
                    place = schematic[y][x : x + 1]
                    if place and place not in "0123456789.":
                        is_part_number = True
            if is_part_number:
                score += int(match.group())
    return score


class GearMemo(NamedTuple):
    gear_x: int
    gear_y: int
    number: int


def get_gear_ratio_sum(day: int = 3, toy: bool = False) -> int:
    """
    Get total value of component numbers.

    519225 was too high.
    """
    schematic = get_data(day=day, toy=toy)
    memos = []
    for rownum, row in enumerate(schematic):
        matches = re.finditer(r"\d+", row)
        for match in matches:
            for y in range(rownum - 1, rownum + 2):
                for x in range(match.start() - 1, match.end() + 1):
                    place = schematic[y][x : x + 1]
                    if place and place == "*":
                        memos.append(
                            GearMemo(gear_x=x, gear_y=y, number=int(match.group()))
                        )
    gears = defaultdict(list)
    for memo in memos:
        gears[f"{memo.gear_x} {memo.gear_y}"].append(memo.number)
    score = 0
    for k, v in gears.items():
        if len(v) == 2:
            score += v[0] * v[1]
    return score
