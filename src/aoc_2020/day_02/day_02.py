from aoc_2020.day_02.data import EXAMPLE, expected
from common.input import get_lines, get_data_file
from common.test import execute_test


def parse_input(data: str) -> list[tuple[int, int, str, str]]:
    lines = get_lines(data)
    result = []
    for line in lines:
        times, character, password = line.split()
        left, right = times.split("-")
        result.append((int(left), int(right), character[0], password))
    return result


def day2_partb(data: str) -> int:
    passwords = parse_input(data)
    valid = 0
    for password in passwords:
        left, right, character, check = password
        is_left = check[left - 1] == character
        is_right = check[right - 1] == character
        valid += 1 if is_left ^ is_right else 0
    return valid


def day2_parta(data: str) -> int:
    passwords = parse_input(data)
    valid = 0
    for password in passwords:
        left, right, character, check = password
        valid += 1 if left <= check.count(character) <= right else 0
    return valid


def main(year: int, day: int, example: bool, part_b: bool) -> int:
    source = EXAMPLE if example else get_data_file(year, day)
    return day2_partb(source) if part_b else day2_parta(source)


if __name__ == "__main__":
    execute_test(main, expected)
