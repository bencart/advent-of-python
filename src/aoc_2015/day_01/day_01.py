from aoc_2015.day_01.data import EXAMPLE, expected
from common.input import get_lines, get_data_file
from common.test import execute_test


def parse_input(data: str) -> str:
    return get_lines(data)[0]


def day1_partb(data: str) -> int:
    instructions = parse_input(data)
    floor = 0
    for i, instruction in enumerate(instructions):
        floor += 1 if instruction == "(" else -1 if instruction == ")" else 0
        if floor < 0:
            return i + 1
    return 0


def day1_parta(data: str) -> int:
    instructions = parse_input(data)
    floor = 0
    for i, instruction in enumerate(instructions):
        floor += 1 if instruction == "(" else -1 if instruction == ")" else 0
    return floor


def main(year: int, day: int, example: bool, part_b: bool) -> int:
    source = EXAMPLE if example else get_data_file(year, day)
    return day1_partb(source) if part_b else day1_parta(source)


if __name__ == "__main__":
    execute_test(main, expected)
