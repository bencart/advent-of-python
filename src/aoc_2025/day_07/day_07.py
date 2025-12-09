from collections import defaultdict

from aoc_2025.day_07.data import EXAMPLE, expected
from common.input import get_data_file, load_dict_grid
from common.test import execute_test
from common.types import Grid


def parse_input(data: str) -> tuple[Grid, int, int, int]:
    grid, rows, cols = load_dict_grid(data)
    return {k: v for k, v in grid.items() if v in ["^"]}, [k for k, v in grid.items() if v == "S"][0][1], rows, cols


def day7_partb(data: str) -> int:
    grid, start, rows, cols = parse_input(data)
    timelines = {start: 1}
    for i in range(1, rows):
        new_timelines = defaultdict(int)
        for timeline, count in timelines.items():
            if grid.get((i, timeline), ".") == "^":
                new_timelines[timeline - 1] += count
                new_timelines[timeline + 1] += count
            else:
                new_timelines[timeline] += count
        timelines = new_timelines
    return sum(timelines.values())


def day7_parta(data: str) -> int:
    grid, start, rows, cols = parse_input(data)
    beams = {start}
    splits = 0
    for i in range(1, rows):
        new_beams = set()
        for beam in beams:
            if grid.get((i, beam), ".") == "^":
                splits += 1
                new_beams.add(beam - 1)
                new_beams.add(beam + 1)
            else:
                new_beams.add(beam)
        beams = new_beams
    return splits


def main(year: int, day: int, example: bool, part_b: bool) -> int:
    source = EXAMPLE if example else get_data_file(year, day)
    return day7_partb(source) if part_b else day7_parta(source)


if __name__ == "__main__":
    execute_test(main, expected)
