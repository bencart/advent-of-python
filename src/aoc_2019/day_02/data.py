EXAMPLE = """
1,9,10,3,2,3,11,0,99,30,40,50
"""

EXAMPLE_B = """
1,9,10,3,1,3,11,0,99,30,40,19690718
"""


def expected(part_b: bool) -> any:
    return 0 if part_b else 3500
