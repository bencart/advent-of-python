EXAMPLE = "R5, L5, R5, R3"
EXAMPLE_B = "R8, R4, R4, R8"


def expected(part_b: bool) -> any:
    return 4 if part_b else 12
