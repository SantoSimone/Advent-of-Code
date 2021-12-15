import heapq
import itertools
import math
from collections import defaultdict
from typing import List

import numpy as np

from python_utils import get_input_as_lines


def get_4n_idx(matrix: np.ndarray, i: int, j: int):
    h, w = matrix.shape[:2]
    return [(i + ii, j + jj) for ii, jj in [(-1, 0), (1, 0), (0, -1), (0, 1)] if
            0 <= i + ii < h and 0 <= j + jj < w]


def d15p1(lines: List[str]):
    grid = np.array([
        list(map(int, line)) for line in lines
    ])

    ret_length = None
    q = []
    heapq.heappush(q, (0, (0, 0)))
    minlength = defaultdict(lambda: math.inf, {(0, 0): 0})
    visited = set()
    while ret_length is None:
        length, pos = heapq.heappop(q)
        if pos == (grid.shape[0] - 1, grid.shape[1] - 1):
            ret_length = length

        visited.add(pos)

        for n in itertools.filterfalse(visited.__contains__, get_4n_idx(grid, pos[0], pos[1])):
            newlength = length + grid[n]
            if newlength < minlength[n]:
                minlength[n] = newlength
                heapq.heappush(q, (newlength, n))

    return ret_length


def d15p2(lines: List[str]):
    # We only need to create a bigger grid
    init_grid = np.array([
        list(map(int, line)) for line in lines
    ])

    h, w = init_grid.shape[:2]
    grid = np.zeros(shape=(h * 5, w * 5))
    for i in range(5):
        for j in range(5):
            new_tile = init_grid + (i + j)
            grid[i * h:(i + 1) * h, j * w:(j + 1) * w] = np.where(new_tile > 9, new_tile - 9, new_tile)

    ret_length = None
    q = []
    heapq.heappush(q, (0, (0, 0)))
    minlength = defaultdict(lambda: math.inf, {(0, 0): 0})
    visited = set()
    while ret_length is None:
        length, pos = heapq.heappop(q)
        if pos == (grid.shape[0] - 1, grid.shape[1] - 1):
            ret_length = length

        visited.add(pos)

        for n in itertools.filterfalse(visited.__contains__, get_4n_idx(grid, pos[0], pos[1])):
            newlength = length + grid[n]
            if newlength < minlength[n]:
                minlength[n] = newlength
                heapq.heappush(q, (newlength, n))

    return ret_length


if __name__ == '__main__':
    lines = get_input_as_lines(15, 2021)
    print(f"Part 1: {d15p1(lines)}")
    print(f"Part 2: {d15p2(lines)}")
