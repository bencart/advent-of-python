EXAMPLE = """
abcdef
bababc
abbcde
abcccd
aabcdd
abcdee
ababab
"""

EXAMPLE_B = """
abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz
"""


def expected(part_b: bool) -> any:
    return 'fgij' if part_b else 12
