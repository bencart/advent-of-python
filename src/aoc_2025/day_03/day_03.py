from aoc_2025.day_03.data import EXAMPLE, expected
from common.input import get_data_file, get_lines
from common.test import execute_test


def parse_input(data: str) -> list[str]:
    return get_lines(data)


def day3(data: str, count: int) -> int:
    input = parse_input(data)
    result = 0
    for line in input:
        indexes = []
        left = 0
        for idx in range(count):
            for val in range(9, -1, -1):
                try:
                    index = line.index(str(val), left, len(line) - (count - 1 - idx))
                    left = index + 1
                    indexes.append(index)
                    break
                except ValueError:
                    pass
        value = [line[idx] for idx in indexes]
        result += int("".join(value))
    return result


def day3_partb(data: str) -> int:
    return day3(data, 12)


def day3_parta(data: str) -> int:
    return day3(data, 2)


def main(year: int, day: int, example: bool, part_b: bool) -> int:
    source = EXAMPLE if example else get_data_file(year, day)
    return day3_partb(source) if part_b else day3_parta(source)


if __name__ == "__main__":
    execute_test(main, expected)
