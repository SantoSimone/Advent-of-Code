import collections
import functools
import itertools
import re
from typing import Tuple, List

import numpy as np

from python_utils import get_input, get_input_as_lines


def intersection(s, t):
    mm = [lambda a, b: -b, max, min, max, min, max, min]
    n = [mm[i](s[i], t[i]) for i in range(7)]
    return None if n[1] > n[2] or n[3] > n[4] or n[5] > n[6] else n


def d22(lines: List[str], is_part1: bool):
    # Heavily based on set theory (https://en.wikipedia.org/wiki/Inclusion%E2%80%93exclusion_principle)
    input_ranges = [[(1 if "on" in line else 0)] + list(map(int, re.findall(r'(-?\d+)+', line))) for line in lines]
    if is_part1:
        input_ranges = [c for c in input_ranges if (np.abs(c[1:]) <= 50).all()]

    cores = []
    for range in input_ranges:
        # Add to core if 'on'
        toadd = [range] if range[0] == 1 else []

        # Compute intersection with every core range
        for core in cores:
            inter = intersection(range, core)

            if inter:
                toadd += [inter]
        cores += toadd

    return sum([active * (maxX - minX + 1) * (maxY - minY + 1) * (maxZ - minZ + 1)
                for active, minX, maxX, minY, maxY, minZ, maxZ in cores])


if __name__ == '__main__':
    lines = get_input_as_lines(22, 2021)
    print(f"Part 1: {d22(lines, True)}")
    print(f"Part 2: {d22(lines, False)}")
