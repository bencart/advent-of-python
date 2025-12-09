from aoc_2019.day_02.data import EXAMPLE, EXAMPLE_B, expected
from aoc_2019.intcode.computer import Computer
from common.input import get_data_file
from common.test import execute_test


def day2_partb(data: str) -> int:
    computer = Computer.from_input(data)
    for j in range(100):
        for i in range(100):
            computer[1] = i
            computer[2] = j
            computer.run()
            if computer[0] == 19690720:
                return 100 * i + j
            computer.reset()
    return 0


def day2_parta(data: str, substitute: dict[int, int]) -> int:
    computer = Computer.from_input(data)
    for k, v in substitute.items():
        computer[k] = v
    computer.run()
    return computer[0]


def main(year: int, day: int, example: bool, part_b: bool) -> int:
    source = EXAMPLE_B if example and part_b else EXAMPLE if example else get_data_file(year, day)
    substitute = {} if example else {1: 12, 2: 2}
    return day2_partb(source) if part_b else day2_parta(source, substitute)


if __name__ == "__main__":
    execute_test(main, expected)
