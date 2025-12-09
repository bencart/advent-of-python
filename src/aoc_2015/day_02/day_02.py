from aoc_2015.day_02.data import EXAMPLE, expected
from common.input import get_lines, get_data_file
from common.test import execute_test


def parse_input(data: str) -> list[tuple[int, int, int]]:
    lines = [l.split('x') for l in get_lines(data)]
    result = []
    for line in lines:
        result.append(sorted((int(line[0]), int(line[1]), int(line[2]))))
    return result


def day2_partb(data: str) -> int:
    packages = parse_input(data)
    result = []
    for l, w, h in packages:
        result.append(2 * l + 2 * w + l * w * h)
    return sum(result)


def day2_parta(data: str) -> int:
    packages = parse_input(data)
    result = []
    for l, w, h in packages:
        result.append(3 * l * w + 2 * l * h + 2 * w * h)
    return sum(result)


def main(year: int, day: int, example: bool, part_b: bool) -> int:
    source = EXAMPLE if example else get_data_file(year, day)
    return day2_partb(source) if part_b else day2_parta(source)


if __name__ == "__main__":
    execute_test(main, expected)
