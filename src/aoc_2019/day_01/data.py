EXAMPLE = """
12
14
1969
100756
"""

EXAMPLE_B = """
14
1969
100756
"""


def expected(part_b: bool) -> any:
    return 51314 if part_b else 34241
