from aoc_2017.day_02.data import EXAMPLE, EXAMPLE_B, expected
from common.input import get_lines, get_data_file
from common.test import execute_test


def parse_input(data: str) -> list[list[int]]:
    lines = [l.split() for l in get_lines(data)]
    result = []
    for line in lines:
        result.append(sorted([int(d) for d in line]))
    return result


def partb_line(line: list[int]) -> int:
    for i in range(len(line) - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            if line[i] % line[j] == 0:
                return line[i] // line[j]
    return 0


def day2_partb(data: str) -> int:
    rows = parse_input(data)
    result = 0
    for row in rows:
        result += partb_line(row)
    return result


def day2_parta(data: str) -> int:
    rows = parse_input(data)
    result = 0
    for row in rows:
        result += row[-1] - row[0]
    return result


def main(year: int, day: int, example: bool, part_b: bool) -> int:
    source = EXAMPLE_B if example and part_b else EXAMPLE if example else get_data_file(year, day)
    return day2_partb(source) if part_b else day2_parta(source)


if __name__ == "__main__":
    execute_test(main, expected)
