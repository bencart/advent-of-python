from aoc_2025.day_05.data import EXAMPLE, expected
from common.input import get_data_file, get_lines
from common.test import execute_test


def parse_input(data: str) -> (list[tuple[int, int]], list[int]):
    lines = get_lines(data)
    ranges = []
    ids = []
    for line in lines:
        if "-" in line:
            parts = line.split("-")
            ranges.append((int(parts[0]), int(parts[1])))
        elif line:
            ids.append(int(line))
    return ranges, ids


def overlap(left: tuple[int, int], right: tuple[int, int]) -> (tuple[int, int], tuple[int, int]):
    if right[0] <= left[1]:
        merged_start = left[0]
        merged_end = max(left[1], right[1])
        return (merged_start, merged_end), (0, 0)
    return left, right


def day5_partb(data: str) -> int:
    ranges, _ = parse_input(data)
    ranges.sort(key=lambda x: x[0])
    result = []
    done = []
    for i in range(len(ranges)):
        if i in done:
            continue
        i_range = ranges[i]
        for j in range(i + 1, len(ranges)):
            if j in done:
                continue
            i_range, j_range = overlap(i_range, ranges[j])
            if j_range == (0, 0):
                done.append(j)
        result.append(i_range[1] - i_range[0] + 1)
    print(result)
    return sum(result)


def day5_parta(data: str) -> int:
    ranges, ids = parse_input(data)
    result = []
    for id in ids:
        for range in ranges:
            if range[0] <= id <= range[1]:
                result.append(id)
                break
    return len(result)


def main(year: int, day: int, example: bool, part_b: bool) -> int:
    source = EXAMPLE if example else get_data_file(year, day)
    return day5_partb(source) if part_b else day5_parta(source)


if __name__ == "__main__":
    execute_test(main, expected)
