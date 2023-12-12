import csv
from pydantic import BaseModel


class ScratchCard(BaseModel):
    wanted: list[int]
    got: list[int]
    num_copies: int = 1

    @property
    def count_matches(self) -> int:
        return len([x for x in self.got if x in self.wanted])

    def get_score(self) -> int:
        got_num = self.count_matches
        if got_num:
            return 2 ** (got_num - 1)
        return 0


def get_data(day: int = 4, toy: bool = True) -> list[ScratchCard]:
    filename = f"{'toy' if toy else ''}data/dec{int(day)}.csv"
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter="|")
        rows = []
        for row in csv_reader:
            rows.append(row)
    cards = []
    for row in rows:
        wanted = [int(x) for x in row[0].strip().split()]
        got = [int(x) for x in row[1].strip().split()]
        cards.append(ScratchCard(wanted=wanted, got=got))
    return cards


def get_score(day: int = 4, toy: bool = False) -> int:
    """
    Get total value of cards.
    """
    cards = get_data(day=day, toy=toy)
    return sum(card.get_score() for card in cards)


def count_up_cards(day: int = 4, toy: bool = False) -> int:
    stacks = get_data(day=day, toy=toy)
    for idx, stack in enumerate(stacks):
        score = stack.count_matches
        for card in range(stack.num_copies):
            for new_index in range(idx + 1, idx + score + 1):
                stacks[new_index].num_copies += 1
    return sum(stack.num_copies for stack in stacks)
