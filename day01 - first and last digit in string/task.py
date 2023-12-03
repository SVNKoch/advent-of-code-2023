import re
import words2num


def findFirstAndLast(string: str, match_pattern: str) -> tuple[str, str]:
    def find_matches(pattern, string):
        match = re.findall(pattern, string)
        if not match:
            raise ValueError(
                f"No match found for pattern: {pattern} in line '{string}'"
            )
        return match

    first_match = find_matches(match_pattern, string)[0]
    last_match = find_matches(match_pattern, string)[-1]
    return first_match, last_match


def toNumbers(number_as_str: str):
    try:
        int(number_as_str)
        return number_as_str
    except ValueError:
        return str(words2num.w2n(number_as_str))


def part1(string: str) -> int:
    reg = r"\d"

    first_match, last_match = findFirstAndLast(string, reg)

    return int(first_match + last_match)


def part2(string: str) -> int:
    reg = r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))"

    first_match, last_match = findFirstAndLast(string, reg)
    first_match = toNumbers(first_match)
    last_match = toNumbers(last_match)

    return int(first_match + last_match)


def main() -> tuple[int, int]:
    sum_part1 = 0
    sum_part2 = 0

    with open("input.txt", "r", encoding="UTF8") as input_file:
        for line in input_file:
            sum_part1 += part1(line)
            sum_part2 += part2(line)

    return sum_part1, sum_part2


if __name__ == "__main__":
    print(main())
