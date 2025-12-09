import os
from collections.abc import Callable

from common.constants import CORRECT, WRONG


def print_result(year: int, day: int, expected: any, answer: any, part: str):
    if expected is not None and answer is not None and expected == answer:
        print(f"{year} Day {day} {part} {expected} == {answer} {CORRECT}")
    elif expected is not None and answer is not None:
        print(f"{year} Day {day} {part} {expected} != {answer} {WRONG}")
    elif answer is not None:
        print(f"{year} Day {day} {part} => {answer}")
    else:
        print(f"{year} Day {day} {part} => Didn't return!")


def execute_test(main: Callable[[int, int, bool, bool], any], expected: Callable[[bool], any]):
    code = main.__code__.co_filename
    code = code.split(os.sep)
    year = int(code[-3].split('_')[1].strip())
    day = int(code[-2].split('_')[1].strip())

    expected_a = expected(False)
    answer_a = main(year, day, True, False)
    print_result(year, day, expected_a, answer_a, "part a example")

    answer_a = main(year, day, False, False)
    print_result(year, day, None, answer_a, "part a")

    expected_b = expected(True)
    answer_b = main(year, day, True, True)
    print_result(year, day, expected_b, answer_b, "part b example")

    answer_b = main(year, day, False, True)
    print_result(year, day, None, answer_b, "part b")
