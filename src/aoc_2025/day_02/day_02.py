import re

from aoc_2025.day_02.data import EXAMPLE, expected
from common.input import get_data_file
from common.test import execute_test

PARTA_RE = re.compile(r'^(.+)\1$')
PARTB_RE = re.compile(r'^(.+)\1+$')


def parse_input(data: str) -> list[list[int]]:
    ids = re.sub(r'\s+', '', data).split(',')
    split = [x.split("-") for x in ids]
    return [[int(i) for i in a] for a in split]


def day2_partb(data: str) -> int:
    input = parse_input(data)
    records = []
    for id_pair in input:
        for i in range(id_pair[0], id_pair[1] + 1):
            compare = str(i)
            if PARTB_RE.match(compare):
                records.append(i)
    return sum(records)


def day2_parta(data: str) -> int:
    input = parse_input(data)
    records = []
    for id_pair in input:
        for i in range(id_pair[0], id_pair[1] + 1):
            compare = str(i)
            if len(compare) % 2 == 1:
                continue
            if PARTA_RE.match(compare):
                records.append(i)
    return sum(records)


def main(year: int, day: int, example: bool, part_b: bool) -> int:
    source = EXAMPLE if example else get_data_file(year, day)
    return day2_partb(source) if part_b else day2_parta(source)


if __name__ == "__main__":
    execute_test(main, expected)
