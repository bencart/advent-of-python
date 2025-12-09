from aoc_2025.day_04.data import EXAMPLE, expected
from common.input import get_data_file, load_dict_grid
from common.test import execute_test
from common.types import Grid, Coordinate


def parse_input(data: str) -> Grid:
    grid, _, _ = load_dict_grid(data)
    return {k: v for k, v in grid.items() if v == "@"}


def removeable(grid: Grid) -> list[Coordinate]:
    result = {}
    for cell in grid.keys():
        row, col = cell
        for r in range(-1, 2, 1):
            for c in range(-1, 2, 1):
                if grid.get((row + r, col + c), "") == "@":
                    result[(row, col)] = result.get((row, col), 0) + 1
    return [k for k, v in result.items() if v < 5]


def day4_partb(data: str) -> int:
    grid = parse_input(data)
    step = removeable(grid)
    result = 0
    while step:
        result += len(step)
        for cell in step:
            grid.pop(cell)
        step = removeable(grid)
    return result


def day4_parta(data: str) -> int:
    grid = parse_input(data)
    return len(removeable(grid))


def main(year: int, day: int, example: bool, part_b: bool) -> int:
    source = EXAMPLE if example else get_data_file(year, day)
    return day4_partb(source) if part_b else day4_parta(source)


if __name__ == "__main__":
    execute_test(main, expected)
