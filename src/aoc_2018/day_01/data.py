EXAMPLE = """
+1
-2
+3
+1
"""

EXAMPLE_B = """
+7
+7
-2
-7
-4
"""


def expected(part_b: bool) -> any:
    return 14 if part_b else 3
