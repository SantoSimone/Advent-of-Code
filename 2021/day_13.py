import re
from typing import List

import numpy as np

from python_utils import get_input_as_lines, splitter


def parse_inputs(lines: List[str]):
    coords, folds = splitter(lines, '')
    coords = [(int(a), int(b))
              for a, b in [coord.split(',') for coord in coords]]
    folds = [(ax, int(v))
             for ax, v in [re.findall(r'([x|y])=(\d+)', fold)[0] for fold in folds]]
    return coords, folds


def d13p1(lines: List[str]):
    coords, folds = parse_inputs(lines)

    grid = np.zeros(shape=(np.max(coords, axis=0) + 1)[::-1])
    for x, y in coords:
        grid[y, x] = 1

    for ax, v in folds[:1]:
        if ax == 'y':
            # the y=v line is removed here
            h = grid.shape[0]
            rest = grid[v + 1:, :]
            flipped = np.flipud(rest)
            grid = grid[:v, :]
            grid[-(h - v):] += flipped
        else:
            w = grid.shape[1]
            rest = grid[:, v + 1:]
            flipped = np.fliplr(rest)
            grid = grid[:, :v]
            grid[:, -(w - v):] += flipped

        grid = np.clip(grid, 0, 1)

    return np.sum(grid)


def d13p2(lines: List[str]):
    coords, folds = parse_inputs(lines)

    grid = np.zeros(shape=(np.max(coords, axis=0) + 1)[::-1])
    for x, y in coords:
        grid[y, x] = 1

    for ax, v in folds:
        if ax == 'y':
            # the y=v line is removed here
            h = grid.shape[0]
            rest = grid[v + 1:, :]
            flipped = np.flipud(rest)
            grid = grid[:v, :]
            grid[-(h - v):] += flipped
        else:
            w = grid.shape[1]
            rest = grid[:, v + 1:]
            flipped = np.fliplr(rest)
            grid = grid[:, :v]
            grid[:, -(w - v):] += flipped

        grid = np.clip(grid, 0, 1)

    for row in grid:
        print(' '.join(['-' if x == 0 else '#' for x in row]))

    return 0


if __name__ == '__main__':
    lines = get_input_as_lines(13, 2021)
    #     lines = """6,10
    # 0,14
    # 9,10
    # 0,3
    # 10,4
    # 4,11
    # 6,0
    # 6,12
    # 4,1
    # 0,13
    # 10,12
    # 3,4
    # 3,0
    # 8,4
    # 1,10
    # 2,14
    # 8,10
    # 9,0
    #
    # fold along y=7
    # fold along x=5""".splitlines()
    print(f"Part 1: {d13p1(lines)}")
    print(f"Part 2: {d13p2(lines)}")
