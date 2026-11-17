"""Main script to calculate and display required wall materials."""

import math

from calc.primitives import volume_parallelepiped, expand_sizes
from calc import get_bricks_count, get_mortar_volume


def main():

    brick_lwh = (250, 120, 65)
    mortar = 10
    wall_lwh = (10000, 510, 3000)
    coefficient = 1.1
    mm3_to_m3 = 1_000_000_000

    wall_volume = volume_parallelepiped(*wall_lwh)

    brick_with_mortar = expand_sizes(brick_lwh, mortar)
    ideal_bricks = get_bricks_count(wall_lwh, brick_with_mortar)

    bricks_to_buy = math.ceil(ideal_bricks * coefficient)

    mortar_volume = get_mortar_volume(wall_lwh, ideal_bricks, brick_lwh)

    wall_m3 = round(wall_volume / mm3_to_m3, 2)
    mortar_m3 = round(mortar_volume / mm3_to_m3, 2)

    print("Wall volume:", wall_m3, "m3")
    print("Bricks to buy", bricks_to_buy, "pcs.")
    print("Mortar volume:", mortar_m3, "m3")


if __name__ == "__main__":
    main()
