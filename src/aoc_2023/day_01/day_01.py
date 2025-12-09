import re

from aoc_2023.day_01.data import EXAMPLE, EXAMPLE_B, VALUES, expected
from common.input import get_lines, get_data_file
from common.test import execute_test

PARTA_RE = re.compile(r'(\d)')
PARTB_RE = re.compile(r'(?=(\d|' + '|'.join(VALUES.keys()) + '))')


def parse_input(data: str) -> list[str]:
    return get_lines(data)


def day1_partb(data: str) -> int:
    lines = parse_input(data)
    result = 0
    for line in lines:
        matches = PARTB_RE.findall(line)
        result += int(VALUES.get(matches[0], matches[0]) +
                      VALUES.get(matches[-1], matches[-1]))
    return result


def day1_parta(data: str) -> int:
    lines = parse_input(data)
    result = 0
    for line in lines:
        matches = PARTA_RE.findall(line)
        result += int(matches[0] + matches[-1])
    return result


def main(year: int, day: int, example: bool, part_b: bool) -> int:
    source = EXAMPLE_B if example and part_b else EXAMPLE if example else get_data_file(year, day)
    return day1_partb(source) if part_b else day1_parta(source)


if __name__ == "__main__":
    execute_test(main, expected)
