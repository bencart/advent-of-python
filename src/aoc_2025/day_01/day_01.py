from aoc_2025.day_01.data import EXAMPLE, expected
from common.input import get_lines, get_data_file
from common.test import execute_test


def parse_input(data: str) -> list[str]:
    return get_lines(data)


def slow(pointer, counter, line) -> (int, int):
    direction = line[0]
    count = int(line[1:])
    movement = 1 if direction == "R" else -1
    for _ in range(count):
        pointer += movement
        if pointer % 100 == 0:
            counter += 1
    return pointer, counter


def fast(pointer, counter, line) -> (int, int):
    direction = line[0]
    count = int(line[1:])
    fulls = count // 100
    singles = count % 100
    singles = -singles if direction == "L" else singles
    target = pointer + singles
    extra = 1 if (pointer > 0 and singles < 0 and target < 0) or \
                 (singles > 0 and target >= 100) or (pointer != 0 and target == 0) else 0
    pointer = target + 100 if target < 0 else target - 100 if target >= 100 else target
    return pointer, counter + fulls + extra


def day1_partb(data: str) -> int:
    lines = parse_input(data)
    p_slow = 50
    c_slow = 0
    p_fast = 50
    c_fast = 0
    for line in lines:
        p_slow, c_slow = slow(p_slow, c_slow, line)
        p_fast, c_fast = fast(p_fast, c_fast, line)
    return c_fast


def day1_parta(data: str) -> int:
    lines = parse_input(data)
    pointer = 50
    counter = 0
    for line in lines:
        direction = line[0]
        count = int(line[1:])
        if direction == "L":
            count *= -1
        pointer += count
        if pointer % 100 == 0:
            counter += 1
    return counter


def main(year: int, day: int, example: bool, part_b: bool) -> int:
    source = EXAMPLE if example else get_data_file(year, day)
    return day1_partb(source) if part_b else day1_parta(source)


if __name__ == "__main__":
    execute_test(main, expected)
