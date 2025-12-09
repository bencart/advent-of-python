from itertools import count

from aoc_2018.day_01.data import EXAMPLE, EXAMPLE_B, expected
from common.input import get_lines, get_data_file
from common.test import execute_test


def parse_input(data: str) -> list[int]:
    lines = get_lines(data)
    return [int(i) for i in lines]


def day1_partb(data: str) -> int:
    digits = parse_input(data)
    visited = set()
    value = 0
    for i in count():
        value += digits[i % len(digits)]
        if value in visited:
            return value
        visited.add(value)
    return value


def day1_parta(data: str) -> int:
    digits = parse_input(data)
    return sum(digits)


def main(year: int, day: int, example: bool, part_b: bool) -> int:
    source = EXAMPLE_B if example and part_b else EXAMPLE if example else get_data_file(year, day)
    return day1_partb(source) if part_b else day1_parta(source)


if __name__ == "__main__":
    execute_test(main, expected)
