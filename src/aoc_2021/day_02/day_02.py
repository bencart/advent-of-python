from aoc_2021.day_02.data import EXAMPLE, expected
from common.input import get_lines, get_data_file
from common.test import execute_test


def parse_input(data: str) -> list[tuple[str, int]]:
    lines = get_lines(data)
    result = []
    for line in lines:
        direction, distance = line.split()
        result.append((direction[0], int(distance)))
    return result


def day2_partb(data: str) -> int:
    instructions = parse_input(data)
    horizontal = 0
    depth = 0
    aim = 0
    for instruction in instructions:
        direction, distance = instruction
        match direction:
            case "f":
                horizontal += distance
                depth += aim * distance
            case "d":
                aim += distance
            case "u":
                aim -= distance
    return horizontal * depth


def day2_parta(data: str) -> int:
    instructions = parse_input(data)
    horizontal = 0
    depth = 0
    for instruction in instructions:
        direction, distance = instruction
        match direction:
            case "f":
                horizontal += distance
            case "d":
                depth += distance
            case "u":
                depth -= distance
    return horizontal * depth


def main(year: int, day: int, example: bool, part_b: bool) -> int:
    source = EXAMPLE if example else get_data_file(year, day)
    return day2_partb(source) if part_b else day2_parta(source)


if __name__ == "__main__":
    execute_test(main, expected)
