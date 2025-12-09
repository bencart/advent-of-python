from aoc_2016.day_01.data import EXAMPLE, EXAMPLE_B, expected
from common.input import get_lines, get_data_file
from common.test import execute_test

L = {(-1, 0): (0, -1), (0, -1): (1, 0), (1, 0): (0, 1), (0, 1): (-1, 0)}
R = {v: k for k, v in L.items()}


def parse_input(data: str) -> list[tuple[str, int]]:
    l = get_lines(data)[0] + ","
    return [(x[0], int(x[1:-1])) for x in l.split()]


def day1_partb(data: str) -> int:
    instructions = parse_input(data)
    direction = (-1, 0)  # face North
    position = (0, 0)
    visited = {position}
    for instruction in instructions:
        turn, distance = instruction
        if turn == "L":
            direction = L[direction]
        else:
            direction = R[direction]
        for i in range(distance):
            position = (position[0] + direction[0], position[1] + direction[1])
            if position in visited:
                return abs(position[0]) + abs(position[1])
            visited.add(position)
    return abs(position[0]) + abs(position[1])


def day1_parta(data: str) -> int:
    instructions = parse_input(data)
    direction = (-1, 0)  # face North
    position = (0, 0)
    for instruction in instructions:
        turn, distance = instruction
        if turn == "L":
            direction = L[direction]
        else:
            direction = R[direction]
        position = (position[0] + direction[0] * distance, position[1] + direction[1] * distance)
    return abs(position[0]) + abs(position[1])


def main(year: int, day: int, example: bool, part_b: bool) -> int:
    source = EXAMPLE_B if example and part_b else EXAMPLE if example else get_data_file(year, day)
    return day1_partb(source) if part_b else day1_parta(source)


if __name__ == "__main__":
    execute_test(main, expected)
