from aoc_2020.day_01.data import EXAMPLE, expected
from common.input import get_lines, get_data_file
from common.test import execute_test


def parse_input(data: str) -> set[int]:
    lines = get_lines(data)
    return set([int(i) for i in lines])


def find_two(digits: set[int], target: int, ignore: int) -> int:
    for k in digits:
        if k == ignore:
            continue
        v = target - k
        if v != k and v != ignore and v in digits:
            return k * v
    return 0


def day1_partb(data: str) -> int:
    digits = parse_input(data)
    for k in digits:
        z = find_two(digits, 2020 - k, k)
        if z:
            return k * z
    return 0


def day1_parta(data: str) -> int:
    digits = parse_input(data)
    return find_two(digits, 2020, 0)


def main(year: int, day: int, example: bool, part_b: bool) -> int:
    source = EXAMPLE if example else get_data_file(year, day)
    return day1_partb(source) if part_b else day1_parta(source)


if __name__ == "__main__":
    execute_test(main, expected)
