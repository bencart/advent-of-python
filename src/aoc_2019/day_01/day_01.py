from aoc_2019.day_01.data import EXAMPLE, EXAMPLE_B, expected
from common.input import get_lines, get_data_file
from common.test import execute_test


def parse_input(data: str) -> list[int]:
    lines = get_lines(data)
    return [int(i) for i in lines]


def fuel(mass: int) -> int:
    result = mass // 3 - 2
    if result <= 0:
        return 0
    return result + fuel(result)


def day1_partb(data: str) -> int:
    digits = parse_input(data)
    return sum([fuel(i) for i in digits])


def day1_parta(data: str) -> int:
    digits = parse_input(data)
    return sum([i // 3 - 2 for i in digits])


def main(year: int, day: int, example: bool, part_b: bool) -> int:
    source = EXAMPLE_B if example and part_b else EXAMPLE if example else get_data_file(year, day)
    return day1_partb(source) if part_b else day1_parta(source)


if __name__ == "__main__":
    execute_test(main, expected)
