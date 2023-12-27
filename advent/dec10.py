from typing import Iterator

import networkx as nx

from advent import dec1


def find_s(map: list[str]) -> tuple[int, int]:
    for y, row in enumerate(map):
        for x, column in enumerate(row):
            if column == "S":
                return x, y
    return -1, -1


PIPES = {
    "|": [(0, -1), (0, 1)],
    "-": [(-1, 0), (1, 0)],
    "L": [(0, -1), (1, 0)],
    "F": [(1, 0), (0, 1)],
    "J": [(-1, 0), (0, -1)],
    "7": [(-1, 0), (0, 1)],
    ".": [],
}


def get_directions(pipe: str, position: tuple[int, int]) -> Iterator[tuple[int, int]]:
    moves: list[tuple[int, int]] = PIPES[pipe]
    for move in moves:
        yield (position[0] + move[0], position[1] + move[1])


def get_pipe_positions(toy: bool = True) -> list[tuple[int, int]]:
    data = dec1.get_data(day=10, toy=toy)
    s_x, s_y = find_s(data)
    positions = []
    next_position = (s_x, s_y + 1)
    while True:
        positions.append(next_position)
        pipe = data[next_position[1]][next_position[0]]
        if pipe == "S":
            return positions
        for direction in get_directions(pipe=pipe, position=next_position):
            if direction not in positions:
                next_position = direction


def get_answer(toy: bool = True) -> int:
    positions = get_pipe_positions(toy=toy)
    return len(positions) // 2
