from math import prod

from aoc_2025.day_06.data import EXAMPLE, expected
from common.input import get_data_file, get_lines
from common.test import execute_test


def parse_parta(data: str) -> list[dict[str, list[int]]]:
    lines = get_lines(data)
    lines = [l.split() for l in lines]
    result = []
    for i in range(len(lines[0])):
        entry = {}
        entry[lines[-1][i]] = [int(l[i]) for l in lines[:-1]]
        result.append(entry)
    return result


def parse_partb(data: str) -> list[dict[str, list[int]]]:
    lines = get_lines(data, strip_lines=False)
    lines = [l + "          " for l in lines]
    length = min([len(l) for l in lines])
    result = []
    numbers = []
    operator = None
    for i in range(length):
        column = "".join([l[i] for l in lines[:-1]]).strip()
        if lines[-1][i].strip():
            operator = lines[-1][i]
        if column:
            numbers.append(int(column))
        elif numbers:
            result.append({operator: numbers})
            numbers = []
    return result


def parse_input(data: str, part_b: bool) -> list[dict[str, list[int]]]:
    return parse_partb(data) if part_b else parse_parta(data)


def calculate(problem: dict[str, list[int]]) -> int:
    return prod(problem.get("*", [0])) + sum(problem.get("+", [0]))


def day6(data: str, part_b: bool) -> int:
    problems = parse_input(data, part_b)
    return sum([calculate(problem) for problem in problems])


def main(year: int, day: int, example: bool, part_b: bool) -> int:
    source = EXAMPLE if example else get_data_file(year, day)
    return day6(source, part_b)


if __name__ == "__main__":
    execute_test(main, expected)
