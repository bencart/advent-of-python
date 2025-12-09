EXAMPLE = """
5 1 9 5
7 5 3
2 4 6 8
"""

EXAMPLE_B = """
5 9 2 8
9 4 7 3
3 8 6 5
"""


def expected(part_b: bool) -> any:
    return 9 if part_b else 18
