from __future__ import annotations
import math


def calculate_number_of_wining_press_options(time: int, distance: int) -> int:
    press_range = find_possible_press_range(time, distance)
    return len(press_range)


def part2():
    pass


def find_possible_press_range(time: int, distance: int) -> range:
    # (time-distance)*distance > record, solve for distance
    # https://www.wolframalpha.com/input?i=%28t-d%29*d+%3E+r%2C+solve+for+d

    intermediate = math.sqrt(time**2 - 4 * distance)
    lower = math.floor(0.5 * (time - intermediate)) + 1
    higher = math.ceil(0.5 * (time + intermediate))

    return range(lower, higher)


def read_input_part_1(string: str) -> list[tuple[int, int]]:
    lines = string.split("\n")
    times = map(int, filter(lambda s: s != "", lines[0].split(":")[1].split(" ")))
    distnaces = map(int, filter(lambda s: s != "", lines[1].split(":")[1].split(" ")))

    return list(zip(times, distnaces))


def read_input_part_2(string: str) -> tuple[int, int]:
    lines = string.split("\n")
    time = int(lines[0].split(":")[1].replace(" ", ""))
    distnace = int(lines[1].split(":")[1].replace(" ", ""))

    return time, distnace


def main() -> tuple[int, int]:
    with open("input.txt", "r", encoding="UTF8") as input_file:
        content = input_file.read()
    races = read_input_part_1(content)
    prod_part1 = math.prod(
        list(map(lambda race: calculate_number_of_wining_press_options(*race), races))
    )
    race = read_input_part_2(content)
    numer_part2 = calculate_number_of_wining_press_options(*race)

    return prod_part1, numer_part2


if __name__ == "__main__":
    print(main())
