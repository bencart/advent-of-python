EXAMPLE = """
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
"""


def expected(part_b: bool) -> any:
    return 1 if part_b else 2
