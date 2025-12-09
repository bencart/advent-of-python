EXAMPLE = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""


def expected(part_b: bool) -> any:
    return 14 if part_b else 3
