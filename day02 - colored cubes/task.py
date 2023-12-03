from __future__ import annotations
from functools import reduce
import re


class Draw:
    def __init__(self, r: int, g: int, b: int):
        self.r: int = r
        self.g: int = g
        self.b: int = b

    def __add__(self, other) -> "Draw":
        return Draw(self.r + other.r, self.g + other.g, self.b + other.b)

    def __eq__(self, other) -> bool:
        return self.r == other.r and self.g == other.g and self.b == other.b

    def __lt__(self, other) -> bool:
        return self.r < other.r or self.g < other.g or self.b < other.b

    def __gt__(self, other) -> bool:
        return self.r > other.r or self.g > other.g or self.b > other.b

    def __str__(self) -> str:
        return f"Draw{{{self.r}, {self.g}, {self.b}}}"

    @staticmethod
    def max(a: Draw, b: Draw) -> Draw:
        return Draw(max(a.r, b.r), max(a.g, b.g), max(a.b, b.b))

    def __repr__(self) -> str:
        return str(self)

    def power(self) -> int:
        return self.r * self.g * self.b


def get_game_number(string: str) -> int:
    match = re.search(r"^Game (\d+):", string)
    if match:
        return int(match.group(1))
    return 0


def toDraws(string: str) -> list[Draw]:
    draws: list[Draw] = []
    for rgb_draw in re.findall(r"(?<=:|;)\s([^;]*)(?=;|$)", string):
        match = re.match(
            r"^(?=(?:.*?(?P<red>\d+) red)?)(?=(?:.*?(?P<green>\d+) green)?)(?=(?:.*?(?P<blue>\d+) blue)?)",
            rgb_draw,
        )
        if match:
            colors = match.groupdict(default="0")
            draws.append(
                Draw(int(colors["red"]), int(colors["green"]), int(colors["blue"]))
            )
    return draws


def part1(draws: list[Draw], game_number: int) -> int:
    max_draws = Draw(12, 13, 14)

    all_smaller = all(map(lambda d: not d > max_draws, draws))
    print(game_number, draws, all_smaller)
    if all_smaller:
        return game_number
    return 0


def part2(draws: list[Draw]):
    max_draw = reduce((Draw.max), draws)
    return max_draw.power()


def main() -> tuple[int, int]:
    sum_part1 = 0
    sum_part2 = 0

    with open("input.txt", "r", encoding="UTF8") as input_file:
        for line in input_file:
            draws: list[Draw] = toDraws(line)
            sum_part1 += part1(draws, get_game_number(line))
            sum_part2 += part2(draws)

    return sum_part1, sum_part2


if __name__ == "__main__":
    print(main())
