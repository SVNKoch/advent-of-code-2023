from __future__ import annotations
from enum import Enum
import re

letter_order = "AKQJT98765432"


def read_input(string: str) -> list[tuple[Hand, int]]:
    l: list[tuple[Hand, int]] = []
    for line in string.split("\n"):
        if line == "":
            continue
        hand = Hand(line.split(" ")[0])
        bid = int(line.split(" ")[1])
        l.append((hand, bid))
    return l


def classify_hand_type(cards: str) -> Type:
    def sort_cards(s):
        frequency = {char: s.count(char) for char in set(s)}
        sorted_string = sorted(
            s, key=lambda char: (-frequency[char], letter_order.find(char))
        )
        return "".join(sorted_string)

    sorted_cards = sort_cards(cards)

    regex_patterns = [
        (Type.FIVE_OF_A_KIND, r"(?=(?P<A>.)(?P=A){4})"),
        (Type.FOUR_OF_A_KIND, r"(?=(?P<A>.)(?P=A){3})"),
        (Type.FULL_HOUSE, r"(?P<A>.)(?P=A){2}(?P<B>.)(?P=B){1}"),
        (Type.THREE_OF_A_KIND, r"(?=(?P<A>.)(?P=A){2})"),
        (Type.TWO_PAIR, r"(?P<A>.)(?P=A){1}(?P<B>.)(?P=B){1}"),
        (Type.ONE_PAIR, r"(?P<A>.)(?P=A){1}"),
    ]

    for label, pattern in regex_patterns:
        if re.search(pattern, sorted_cards):
            return label

    return Type.HIGH_CARD


def classify_hand_strength(cards: str) -> int:
    reversed_order = letter_order[::-1]

    char_to_index = {
        char: str(reversed_order.index(char)).zfill(2) for char in reversed_order
    }

    converted = [char_to_index[char] for char in cards]

    return int("".join(converted))


class Type(Enum):
    FIVE_OF_A_KIND = 6
    FOUR_OF_A_KIND = 5
    FULL_HOUSE = 4
    THREE_OF_A_KIND = 3
    TWO_PAIR = 2
    ONE_PAIR = 1
    HIGH_CARD = 0

    def __lt__(self, other: Type) -> bool:
        return self.value < other.value


class Hand:
    def __init__(self, cards: str) -> None:
        self.type = classify_hand_type(cards)
        self.strength = classify_hand_strength(cards)

    def __lt__(self, other: Hand) -> bool:
        if self.type == other.type:
            return self.strength < other.strength
        return self.type < other.type


def part1(string: str) -> int:
    summed = 0
    hands_bids = read_input(string)
    hands_bids.sort(key=lambda x: x[0])
    for index, (_, bid) in enumerate(hands_bids):
        rank = index + 1
        summed += rank * bid
    return summed


def main() -> int:
    with open("input.txt", "r", encoding="UTF8") as input_file:
        content = input_file.read()
    sum_part1 = part1(content)

    return sum_part1


if __name__ == "__main__":
    print(main())
