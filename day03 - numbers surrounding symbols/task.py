from __future__ import annotations
import re
import math


def part1(field: list[str]) -> int:
    return sum(find_part_numbers(field))


def part2(field: list[str]) -> int:
    return sum(find_part_numbers(field, True))


def find_part_numbers(field: list[str], is_part2: bool = False) -> list[int]:
    dimension = calculate_dimensions(field)

    number_matches_on_lines = [list(re.finditer(r"\d+", line)) for line in field]

    if is_part2:
        symbol_locations = find_symbols(field, r"\*")
    else:
        symbol_locations = find_symbols(field)

    part_numbers: list[int] = []

    for symbol_location in symbol_locations:
        sourroundings = sourrounding(symbol_location, dimension)

        line_number_matches_sourrounding = set()
        for location in sourroundings:
            number_matches_on_line = number_matches_on_lines[location[0]]

            def lies_in_span(match, index):
                start, end = match.span()
                return start <= index < end

            # pylint: disable=cell-var-from-loop
            number_match_at_location = map(
                lambda m: (location[0], m),
                filter(
                    lambda match: lies_in_span(match, location[1]),
                    number_matches_on_line,
                ),
            )
            line_number_matches_sourrounding.update(number_match_at_location)

        if is_part2 and len(line_number_matches_sourrounding) != 2:
            continue

        sourrounding_part_numbers: list[int] = []
        for line_muber, number_match_sourrounding in line_number_matches_sourrounding:
            start, end = number_match_sourrounding.span()
            part_number: str = field[line_muber][start:end]
            sourrounding_part_numbers.append(int(part_number))

        if is_part2:
            part_numbers.append(math.prod(sourrounding_part_numbers))
        else:
            part_numbers.extend(sourrounding_part_numbers)

    return part_numbers


def find_symbols(
    field: list[str], regex: str = r"[*&$\-+%/#=@]"
) -> list[tuple[int, int]]:
    result: list[tuple[int, int]] = []
    for line_number, line in enumerate(field):
        result.extend(
            list(
                map(
                    # pylint: disable=cell-var-from-loop
                    lambda match: (line_number, match.span()[0]),
                    list(re.finditer(regex, line)),
                )
            )
        )
    return result


def sourrounding(
    pos: tuple[int, int], dimension: tuple[int, int]
) -> list[tuple[int, int]]:
    dirs = [-1, 0, 1]

    combinations = [(x, y) for x in dirs for y in dirs if not x == y == 0]

    available_positions = map(
        lambda dir: (pos[0] + dir[0], pos[1] + dir[1]), combinations
    )
    available_positions = filter(
        lambda pos: 0 <= pos[0] < dimension[0] and 0 <= pos[1] < dimension[1],
        available_positions,
    )

    return list(available_positions)


def calculate_dimensions(field: list[str]) -> tuple[int, int]:
    return len(field), len(field[0])


def main() -> tuple[int, int]:
    with open("input.txt", "r", encoding="UTF8") as input_file:
        field = input_file.readlines()

    return part1(field), part2(field)


if __name__ == "__main__":
    print(main())
