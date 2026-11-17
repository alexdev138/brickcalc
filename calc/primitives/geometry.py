"""A small module with functions for calculating rectangle area,
parallelepiped volume, and expanding tuple values."""

import sys


def area_rectangle(length: int | float, width: int | float) -> int | float:
    return abs(length) * abs(width)


def volume_parallelepiped(
    length: int | float, width: int | float, height: int | float
) -> int | float:
    return abs(length) * abs(width) * abs(height)


def expand_sizes(x: tuple, y: float | int) -> tuple:
    if type(x) == tuple:
        return tuple(map(lambda a: a + y, x))
    else:
        sys.exit(1)

