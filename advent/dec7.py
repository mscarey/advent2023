from collections import Counter
import csv
from typing import Self
from pydantic import BaseModel, field_validator


class CardMemo(BaseModel):
    hand: str
    bid: int

    @property
    def kind(self) -> str:
        cards = Counter(self.hand)
        most_common = [str(x[1]) for x in cards.most_common(2)]
        return "".join(most_common)

    @field_validator("hand")
    @classmethod
    def card_letters(cls, v) -> str:
        return (
            v.replace("T", "B")
            .replace("J", "C")
            .replace("Q", "D")
            .replace("K", "E")
            .replace("A", "F")
        )

    def __lt__(self, other: Self) -> bool:
        if self.kind < other.kind:
            return True
        if self.kind == other.kind and self.hand < other.hand:
            return True
        return False


def get_data(day: int = 7, toy: bool = True) -> list[CardMemo]:
    filename = f"{'toy' if toy else ''}data/dec{int(day)}.csv"
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=" ")
        rows = []
        for row in csv_reader:
            rows.append(CardMemo(hand=row[0], bid=int(row[1])))
    return rows


def get_answer(day: int = 7, toy: bool = True) -> int:
    data = get_data(day=day, toy=toy)
    result = sorted(data)
    scores = []
    for rank, hand in enumerate(result):
        scores.append((rank + 1) * hand.bid)
    return sum(scores)
