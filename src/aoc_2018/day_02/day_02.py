from collections import defaultdict

from aoc_2018.day_02.data import EXAMPLE, EXAMPLE_B, expected
from common.input import get_lines, get_data_file
from common.test import execute_test


def parse_input(data: str) -> list[str]:
    return get_lines(data)


def day2_partb(data: str) -> str:
    records = parse_input(data)
    for i in range(len(records)):
        for j in range(i + 1, len(records)):
            diff = 0
            pos = 0
            for k in range(len(records[i])):
                if records[i][k] != records[j][k]:
                    diff += 1
                    pos = k
                    if diff > 1:
                        break
            if diff == 1:
                return records[i][:pos] + records[i][pos + 1:]
    return ""


def find_letters(row: str) -> dict[str, int]:
    r = defaultdict(int)
    for c in row:
        r[c] += 1
    return r


def day2_parta(data: str) -> int:
    records = parse_input(data)
    twos = 0
    threes = 0
    for row in records:
        letters = find_letters(row)
        twos += 1 if 2 in letters.values() else 0
        threes += 1 if 3 in letters.values() else 0
    return twos * threes


def main(year: int, day: int, example: bool, part_b: bool) -> any:
    source = EXAMPLE_B if example and part_b else EXAMPLE if example else get_data_file(year, day)
    return day2_partb(source) if part_b else day2_parta(source)


if __name__ == "__main__":
    execute_test(main, expected)
