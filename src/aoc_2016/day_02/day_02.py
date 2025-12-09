from aoc_2016.day_02.data import EXAMPLE, expected
from common.input import get_lines, get_data_file
from common.test import execute_test

KEYPAD = {(0, 0): "1", (0, 1): "2", (0, 2): "3",
          (1, 0): "4", (1, 1): "5", (1, 2): "6",
          (2, 0): "7", (2, 1): "8", (2, 2): "9"}
DIAMOND = {(0, 2): "1",
           (1, 1): "2", (1, 2): "3", (1, 3): "4",
           (2, 0): "5", (2, 1): "6", (2, 2): "7", (2, 3): "8", (2, 4): "9",
           (3, 1): "A", (3, 2): "B", (3, 3): "C",
           (4, 2): "D"}
DIRECTION = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}


def parse_input(data: str) -> list[tuple[str, int]]:
    return get_lines(data)


def day2(data: str, keypad: dict[tuple[int, int], str], start: tuple[int, int]) -> str:
    instructions = parse_input(data)
    code = ""
    position = start
    for instruction_line in instructions:
        for instruction in instruction_line:
            movement = DIRECTION.get(instruction)
            new_position = position[0] + movement[0], position[1] + movement[1]
            if new_position in keypad:
                position = new_position
        code += keypad[position]
    return code


def day2_partb(data: str) -> str:
    return day2(data, DIAMOND, (2, 0))


def day2_parta(data: str) -> str:
    return day2(data, KEYPAD, (1, 1))


def main(year: int, day: int, example: bool, part_b: bool) -> int:
    source = EXAMPLE if example else get_data_file(year, day)
    return day2_partb(source) if part_b else day2_parta(source)


if __name__ == "__main__":
    execute_test(main, expected)
