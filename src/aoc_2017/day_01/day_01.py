from aoc_2017.day_01.data import EXAMPLE, EXAMPLE_B, expected
from common.input import get_lines, get_data_file
from common.test import execute_test


def parse_input(data: str) -> str:
    return get_lines(data)[0]


def day1_partb(data: str) -> int:
    digits = parse_input(data)
    offset = len(digits) // 2
    matches = 0
    for i in range(len(digits)):
        check = (i + offset) % len(digits)
        if digits[i] == digits[check]:
            matches += int(digits[i])
    return matches


def day1_parta(data: str) -> int:
    digits = parse_input(data)
    matches = 0
    for i in range(len(digits)):
        check = (i + 1) % len(digits)
        if digits[i] == digits[check]:
            matches += int(digits[i])
    return matches


def main(year: int, day: int, example: bool, part_b: bool) -> int:
    source = EXAMPLE_B if example and part_b else EXAMPLE if example else get_data_file(year, day)
    return day1_partb(source) if part_b else day1_parta(source)


if __name__ == "__main__":
    execute_test(main, expected)
