from aoc_2022.day_02.data import EXAMPLE, expected
from common.input import get_lines, get_data_file
from common.test import execute_test

LOSS = 0
DRAW = 3
WIN = 6

R = 1
P = 2
S = 3

PART_A = {"A": {"X": DRAW + R, "Y": WIN + P, "Z": LOSS + S},
          "B": {"X": LOSS + R, "Y": DRAW + P, "Z": WIN + S},
          "C": {"X": WIN + R, "Y": LOSS + P, "Z": DRAW + S}}

PART_B = {"A": {"X": LOSS + S, "Y": DRAW + R, "Z": WIN + P},
          "B": {"X": LOSS + R, "Y": DRAW + P, "Z": WIN + S},
          "C": {"X": LOSS + P, "Y": DRAW + S, "Z": WIN + R}}


def parse_input(data: str) -> list[list[str]]:
    return [x.split() for x in get_lines(data)]


def day2_partb(data: str) -> int:
    lines = parse_input(data)
    score = 0
    for line in lines:
        elf, player = line
        score += PART_B.get(elf).get(player)
    return score


def day2_parta(data: str) -> int:
    lines = parse_input(data)
    score = 0
    for line in lines:
        elf, player = line
        score += PART_A.get(elf).get(player)
    return score


def main(year: int, day: int, example: bool, part_b: bool) -> int:
    source = EXAMPLE if example else get_data_file(year, day)
    return day2_partb(source) if part_b else day2_parta(source)


if __name__ == "__main__":
    execute_test(main, expected)
