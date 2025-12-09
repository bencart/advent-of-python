from collections import defaultdict

from aoc_2024.day_01.data import EXAMPLE, expected
from common.input import get_lines, get_data_file
from common.test import execute_test


def parse_input(data: str) -> tuple[list[int], list[int]]:
    columns = [l.split() for l in get_lines(data)]
    left = [int(c[0].strip()) for c in columns]
    right = [int(c[1].strip()) for c in columns]
    return sorted(left), sorted(right)


def day1_partb(data: str) -> int:
    left_column, right_column = parse_input(data)
    right = defaultdict(int)
    for value in right_column:
        right[value] += 1
    result = 0
    for value in left_column:
        result += value * right[value]
    return result


def day1_parta(data: str) -> int:
    left_column, right_column = parse_input(data)
    distances = []
    for i in range(len(left_column)):
        distances.append(abs(left_column[i] - right_column[i]))
    return sum(distances)


def main(year: int, day: int, example: bool, part_b: bool) -> int:
    source = EXAMPLE if example else get_data_file(year, day)
    return day1_partb(source) if part_b else day1_parta(source)


if __name__ == "__main__":
    execute_test(main, expected)
