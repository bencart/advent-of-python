from aoc_2021.day_01.data import EXAMPLE, expected
from common.input import get_lines, get_data_file
from common.test import execute_test


def parse_input(data: str) -> list[int]:
    lines = get_lines(data)
    return [int(i) for i in lines]


def day1_partb(data: str) -> int:
    digits = parse_input(data)
    result = 0
    for i in range(len(digits) - 3):
        result += 1 if digits[i] < digits[i + 3] else 0
    return result


def day1_parta(data: str) -> int:
    digits = parse_input(data)
    result = 0
    for i in range(len(digits) - 1):
        result += 1 if digits[i] < digits[i + 1] else 0
    return result


def main(year: int, day: int, example: bool, part_b: bool) -> int:
    source = EXAMPLE if example else get_data_file(year, day)
    return day1_partb(source) if part_b else day1_parta(source)


if __name__ == "__main__":
    execute_test(main, expected)
