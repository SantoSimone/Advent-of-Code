import itertools
import re
from collections import defaultdict
from typing import List, Tuple, Dict

import numpy as np

from python_utils import get_input_as_lines, splitter, parse_ints, get_input


def neighbors(i: int, j: int) -> List[Tuple[int, int]]:
    return [(i + ii, j + jj)
            for ii, jj in itertools.product([-1, 0, 1], [-1, 0, 1])
            if 0 <= i + ii < 10 and 0 <= j + jj < 10 and (ii, jj) != (0, 0)]


def d11p1(lines: List[str]):
    octopuses = np.array(
        [list(map(int, re.findall(r'\d', line))) for line in lines]
    )

    num_flashes = 0
    for step in range(1, 101):
        octopuses += 1
        flashed = set()

        # Compute flashes
        while True:
            should_flash = set(zip(*[list(indices) for indices in np.where(octopuses > 9)]))
            should_flash = should_flash.difference(flashed)
            if len(should_flash) == 0:
                break

            for i, j in sorted(should_flash):
                octopuses[list(zip(*neighbors(i, j)))] += 1
            flashed = flashed.union(should_flash)

        # Update flashed
        num_flashes += len(flashed)
        octopuses[list(zip(*flashed))] = 0

    return num_flashes


def d11p2(lines: List[str]):
    octopuses = np.array(
        [list(map(int, re.findall(r'\d', line))) for line in lines]
    )

    step = 1
    while True:
        octopuses += 1
        flashed = set()

        # Compute flashes
        while True:
            should_flash = set(zip(*[list(indices) for indices in np.where(octopuses > 9)]))
            should_flash = should_flash.difference(flashed)
            if len(should_flash) == 0:
                break

            for i, j in sorted(should_flash):
                octopuses[list(zip(*neighbors(i, j)))] += 1
            flashed = flashed.union(should_flash)

        # Check exit
        if len(flashed) == np.prod(octopuses.shape[:2]):
            return step

        # Update flashed
        octopuses[list(zip(*flashed))] = 0
        step += 1


if __name__ == '__main__':
    lines = get_input_as_lines(11, 2021)
    print(f"Part 1: {d11p1(lines)}")
    print(f"Part 2: {d11p2(lines)}")
