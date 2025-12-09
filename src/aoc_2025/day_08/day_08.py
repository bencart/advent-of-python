import math
from collections import defaultdict

from aoc_2025.day_08.data import EXAMPLE, expected
from common.input import get_data_file, get_lines
from common.test import execute_test


def parse_input(data: str) -> list[tuple[int, int, int]]:
    lines = get_lines(data)
    result = []
    for line in lines:
        x, y, z = line.split(",", 3)
        result.append((int(x), int(y), int(z)))
    return result


def calculate_distance(left: tuple[int, int, int], right: tuple[int, int, int]) -> float:
    return math.sqrt(
        (left[0] - right[0]) ** 2 +
        (left[1] - right[1]) ** 2 +
        (left[2] - right[2]) ** 2
    )


def get_distance_map(junctions: list[tuple[int, int, int]]):
    distances = defaultdict(list)
    junction_map = {}
    for i in range(len(junctions)):
        junction_map[i] = {i}
        for j in range(i + 1, len(junctions)):
            distance = calculate_distance(junctions[i], junctions[j])
            distances[distance].append((i, j))
    return distances, junction_map


def day8_partb(data: str) -> int:
    junctions = parse_input(data)
    distances, junction_map = get_distance_map(junctions)
    distance_values = sorted(distances.keys())
    for i in range(len(distance_values)):
        distance = distance_values[i]
        nodes = distances[distance][0]
        if junction_map[nodes[0]] != junction_map[nodes[1]]:
            joined = junction_map[nodes[0]] | junction_map[nodes[1]]
            if len(joined) == len(junctions):
                return junctions[nodes[0]][0] * junctions[nodes[1]][0]
            for node in joined:
                junction_map[node] = joined


def day8_parta(data: str, count: int) -> int:
    junctions = parse_input(data)
    distances, junction_map = get_distance_map(junctions)
    distance_values = sorted(distances.keys())
    for i in range(count):
        distance = distance_values[i]
        nodes = distances[distance][0]
        if junction_map[nodes[0]] != junction_map[nodes[1]]:
            joined = junction_map[nodes[0]] | junction_map[nodes[1]]
            for node in joined:
                junction_map[node] = joined
    visited = set()
    lengths = []
    for network in junction_map.values():
        if str(network) in visited:
            continue
        visited.add(str(network))
        lengths.append(len(network))
    lengths = sorted(lengths, reverse=True)[:3]
    return math.prod(lengths)


def main(year: int, day: int, example: bool, part_b: bool) -> int:
    source = EXAMPLE if example else get_data_file(year, day)
    count = 10 if example else 1000
    return day8_partb(source) if part_b else day8_parta(source, count)


if __name__ == "__main__":
    execute_test(main, expected)
