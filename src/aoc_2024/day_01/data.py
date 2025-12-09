EXAMPLE = """
3   4
4   3
2   5
1   3
3   9
3   3
"""


def expected(part_b: bool) -> any:
    return 31 if part_b else 11
