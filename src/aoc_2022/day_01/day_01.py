from aoc_2022.day_01.data import EXAMPLE, expected
from common.input import get_lines, get_data_file
from common.test import execute_test


def parse_input(data: str) -> list[str]:
    return get_lines(data, strip_empty=False) + ['']


def day1_partb(data: str) -> int:
    lines = parse_input(data)
    most_calories = [0, 0, 0]
    current = 0
    for line in lines:
        if not line:
            most_calories.append(current)
            most_calories = list(sorted(most_calories, reverse=True)[:3])
            current = 0
        else:
            current += int(line)
    return sum(most_calories)


def day1_parta(data: str) -> int:
    lines = parse_input(data)
    most_calories = 0
    current = 0
    for line in lines:
        if not line:
            most_calories = current if current > most_calories else most_calories
            current = 0
        else:
            current += int(line)
    return most_calories


def main(year: int, day: int, example: bool, part_b: bool) -> int:
    source = EXAMPLE if example else get_data_file(year, day)
    return day1_partb(source) if part_b else day1_parta(source)


if __name__ == "__main__":
    execute_test(main, expected)
