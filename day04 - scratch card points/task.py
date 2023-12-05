from __future__ import annotations
import math


def part1(string: str) -> int:
    _, winning_numbers, my_numbers = read_card(string)
    count = len(get_winning_subset(winning_numbers, my_numbers))
    return math.floor(2 ** (count - 1))


class TicketList:
    def __init__(self, length: int) -> None:
        self.tickets = [1] * length

    def increase(self: TicketList, game_number: int, size: int) -> TicketList:
        self.tickets[game_number : game_number + size] = map(
            lambda v: v + self.tickets[game_number - 1],
            self.tickets[game_number : game_number + size],
        )
        return self


def part2(tl: TicketList, string: str) -> TicketList:
    game_number, winning_numbers, my_numbers = read_card(string)
    count = len(get_winning_subset(winning_numbers, my_numbers))
    tl.increase(game_number, count)
    return tl


def read_card(string: str) -> tuple[int, list[int], list[int]]:
    game, rest = string.split(":")

    card_number = int(list(filter(lambda x: x != "", game.split(" ")))[1])

    winning_numbers, my_numbers = map(
        lambda l: list(map(int, filter(lambda v: v != "", l.split(" ")))),
        rest.split("|"),
    )

    return card_number, winning_numbers, my_numbers


def get_winning_subset(winning_numbers: list[int], my_numbers: list[int]) -> list[int]:
    return [x for x in winning_numbers if x in my_numbers]


def main() -> tuple[int, int]:
    sum_part1 = 0

    with open("input.txt", "r", encoding="UTF8") as input_file:
        lines = input_file.readlines()
    tl = TicketList(len(lines))
    for line in lines:
        sum_part1 += part1(line)
        part2(tl, line)

    return sum_part1, sum(tl.tickets)


if __name__ == "__main__":
    print(main())
