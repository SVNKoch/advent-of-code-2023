from __future__ import annotations
from functools import reduce
import re


def part1(lines: list[str]) -> int:
    path = lines[0].strip()
    network = read_map(lines[2:])
    return step_count_till_zzz(path, network, "AAA")


def part2():
    pass


def step_count_till_zzz(
    path: str, network: dict[str, tuple[str, str]], start: str
) -> int:
    step_count = 0
    current_node = start
    while True:
        steps, end_node = follow_path_to_zzz(path, network, current_node)
        step_count += steps
        if end_node == "ZZZ":
            return step_count
        current_node = end_node


def follow_path_to_zzz(
    path: str, network: dict[str, tuple[str, str]], start: str
) -> tuple[int, str]:
    current_node = start
    for index, direction in enumerate(path):
        direction_index = 0 if direction == "L" else 1
        if current_node == "ZZZ":
            return index, current_node
        current_node = network[current_node][direction_index]
    return len(path), current_node


def read_map(lines: list[str]) -> dict[str, tuple[str, str]]:
    network: dict[str, tuple[str, str]] = {}
    for line in lines:
        match = re.match(r"([A-Z]+) = \(([A-Z]+), ([A-Z]+)\)", line)
        if not match:
            raise ValueError(f"invalid input line '{line}'")
        a, b, c = match.groups()
        network[a] = (b, c)
    return network


def main() -> tuple[int, int]:
    with open("input.txt", "r", encoding="UTF8") as input_file:
        lines = input_file.readlines()
    step_count = part1(lines)

    return step_count, 0


if __name__ == "__main__":
    print(main())
    with open("log.txt", "w") as f:
        f.write(my_log)
