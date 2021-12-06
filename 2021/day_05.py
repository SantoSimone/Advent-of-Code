import re
from typing import List, Tuple

import numpy as np

from python_utils import get_input_as_lines, splitter, parse_ints


def d5p1(lines: List[str]):
    grid = np.zeros(shape=(1000, 1000), dtype=int)  # random shape, just fit in
    for line in lines:
        x1, y1, x2, y2 = parse_ints(line)
        if not (x1 == x2 or y1 == y2):
            continue

        if y1 > y2:
            y1, y2 = y2, y1
        if x1 > x2:
            x1, x2 = x2, x1
        grid[y1:y2 + 1, x1:x2 + 1] += 1

    return np.sum(grid > 1)


def d5p2(lines: List[str]):
    grid = np.zeros(shape=(1000, 1000), dtype=int)  # random shape, just fit in
    for line in lines:
        x1, y1, x2, y2 = parse_ints(line)
        if x1 != x2 and y1 != y2:
            y_indices = range(y1, y2 + 1) if y2 > y1 else list(reversed(range(y2, y1 + 1)))
            x_indices = range(x1, x2 + 1) if x2 > x1 else list(reversed(range(x2, x1 + 1)))
            grid[y_indices, x_indices] += 1
        else:
            if y1 > y2:
                y1, y2 = y2, y1
            if x1 > x2:
                x1, x2 = x2, x1

            grid[y1:y2 + 1, x1:x2 + 1] += 1

    return np.sum(grid > 1)


if __name__ == '__main__':
    lines = get_input_as_lines(5, 2021)
    print(f"Part 1: {d5p1(lines)}")
    print(f"Part 2: {d5p2(lines)}")
