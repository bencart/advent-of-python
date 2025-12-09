from common.types import Coordinate, Vector


def add_direction(c: Coordinate, d: str) -> Vector:
    return (*c, d)


def sum_c(a: Coordinate, b: Coordinate) -> Coordinate:
    return (a[0] + b[0], a[1] + b[1])


def sub_c(a: Coordinate, b: Coordinate) -> Coordinate:
    return (a[0] - b[0], a[1] - b[1])


def man_d(a: Coordinate, b: Coordinate) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
