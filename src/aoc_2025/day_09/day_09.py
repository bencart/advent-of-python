from aoc_2025.day_09.data import EXAMPLE, expected
from common.input import get_data_file, get_lines
from common.test import execute_test
from common.types import Coordinate


def parse_input(data: str) -> list[Coordinate]:
    lines = get_lines(data)
    result = []
    for line in lines:
        x, y = line.split(",", 3)
        result.append((int(x), int(y)))
    return result


def calculate_area(left: Coordinate, right: Coordinate) -> int:
    return (abs(left[0] - right[0]) + 1) * (abs(left[1] - right[1]) + 1)


def point_inside(point: Coordinate, outline: set[Coordinate]) -> bool:
    crossings = 0
    is_inside = False
    for x in range(point[0] + 1):
        on_outline = (x, point[1]) in outline
        if on_outline and not is_inside:
            is_inside = True
            crossings += 1
        elif not on_outline:
            is_inside = False
    return crossings % 2 == 1


def fully_inside(left: Coordinate, right: Coordinate, outline: set[Coordinate]) -> bool:
    min_x, max_x = sorted([left[0], right[0]])
    min_y, max_y = sorted([left[1], right[1]])

    for point in outline:
        if min_x < point[0] < max_x and min_y < point[1] < max_y:
            return False
    return point_inside((min_x, min_y), outline)


def compress_grid(tiles: list[Coordinate]) -> tuple[list[Coordinate], dict[Coordinate, Coordinate]]:
    xs = sorted([t[0] for t in tiles])
    ys = sorted([t[1] for t in tiles])
    lookup_x = {v: i for i, v in enumerate(sorted(xs))}
    lookup_y = {v: i for i, v in enumerate(sorted(ys))}
    new_tiles = []
    lookups = {}
    for tile in tiles:
        x = lookup_x[tile[0]]
        y = lookup_y[tile[1]]
        new_tiles.append((x, y))
        lookups[(x, y)] = tile
    return new_tiles, lookups


def get_outline(tiles: list[Coordinate]) -> set[Coordinate]:
    outline = set(tiles)
    for i in range(-1, len(tiles) - 1):
        this_tile = tiles[i]
        next_tile = tiles[i + 1]

        tx, nx = sorted([this_tile[0], next_tile[0]])
        ty, ny = sorted([this_tile[1], next_tile[1]])

        for x in range(tx, nx + 1):
            for y in range(ty, ny + 1):
                outline.add((x, y))
    return outline


def day9_partb(data: str) -> int:
    tiles = parse_input(data)
    compressed, lookup = compress_grid(tiles)
    outline = get_outline(compressed)

    max_area = 0
    for i in range(len(compressed)):
        for j in range(i + 1, len(compressed)):
            area = calculate_area(lookup.get(compressed[i]), lookup.get(compressed[j]))
            if area > max_area and fully_inside(compressed[i], compressed[j], outline):
                max_area = area
    return max_area


def day9_parta(data: str) -> int:
    tiles = parse_input(data)
    max_area = 0
    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            area = calculate_area(tiles[i], tiles[j])
            if area > max_area:
                max_area = area
    return max_area


def main(year: int, day: int, example: bool, part_b: bool) -> int:
    source = EXAMPLE if example else get_data_file(year, day)
    return day9_partb(source) if part_b else day9_parta(source)


if __name__ == "__main__":
    execute_test(main, expected)
