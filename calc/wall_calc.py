"""
Module for calculating the number of bricks and mortar volume.
"""

from calc.primitives.geometry import volume_parallelepiped

__all__ = ["get_bricks_count","get_mortar_volume"]

def get_bricks_count(wall_sizes: tuple, brick_with_gap_sizes: tuple) -> float:

    wall_volume = volume_parallelepiped(*wall_sizes)
    brick_volume = volume_parallelepiped(*brick_with_gap_sizes)

    return wall_volume / brick_volume


def get_mortar_volume(
    wall_sizes: tuple, bricks_count: float, clean_brick_sizes: tuple
) -> float:

    wall_volume = volume_parallelepiped(*wall_sizes)

    clean_brick_volume = volume_parallelepiped(*clean_brick_sizes)

    total_bricks_volume = bricks_count * clean_brick_volume

    return wall_volume - total_bricks_volume
