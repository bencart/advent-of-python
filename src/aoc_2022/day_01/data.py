EXAMPLE = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""


def expected(part_b: bool) -> any:
    return 45000 if part_b else 24000
