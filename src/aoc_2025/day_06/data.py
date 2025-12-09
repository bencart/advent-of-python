EXAMPLE = """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +   
"""


def expected(part_b: bool) -> any:
    return 3263827 if part_b else 4277556
