import itertools
import re
from collections import defaultdict
from typing import List, Tuple, Dict

import numpy as np

from python_utils import get_input_as_lines, splitter, parse_ints, get_input


def get_4n_idx(matrix: np.ndarray, i: int, j: int):
    h, w = matrix.shape[:2]
    return [(i + ii, j + jj) for ii, jj in [(-1, 0), (1, 0), (0, -1), (0, 1)] if
            0 <= i + ii < h and 0 <= j + jj < w]


def get_4n(matrix: np.ndarray, i: int, j: int):
    h, w = matrix.shape[:2]
    return [matrix[i + ii, j + jj] for ii, jj in [(-1, 0), (1, 0), (0, -1), (0, 1)] if
            0 <= i + ii < h and 0 <= j + jj < w]


def d9p1(lines: List[str]):
    matrix = np.array([
        list(map(int, re.findall(r'\d', line))) for line in lines
    ])

    h, w = matrix.shape[:2]

    min_ = [(i, j) for i, j in itertools.product(range(h), range(w)) if matrix[i, j] < min(get_4n(matrix, i, j))]
    return sum([matrix[i, j] + 1 for i, j in min_])


def d9p2(lines: List[str]):
    matrix = np.array([
        list(map(int, re.findall(r'\d', line))) for line in lines
    ])

    h, w = matrix.shape[:2]

    min_ = [(i, j) for i, j in itertools.product(range(h), range(w)) if matrix[i, j] < min(get_4n(matrix, i, j))]

    def rec(i, j):
        if np.all([matrix[ii, jj] == 9 for ii, jj in get_4n_idx(matrix, i, j)]):
            return [(i, j)]

        n = [(ii, jj) for (ii, jj) in get_4n_idx(matrix, i, j) if matrix[ii, jj] < 9]

        ret = {(i, j)}
        for ii, jj in n:
            if matrix[i, j] < matrix[ii, jj] < 9:
                ret = ret.union(rec(ii, jj))

        return ret

    r2 = []
    for i, j in min_:
        r2.append(len(rec(i, j)))
    # r2 = sorted([rec(i, j)[0] for i, j in min_])

    return np.prod(sorted(r2)[-3:])


if __name__ == '__main__':
    lines = get_input_as_lines(9, 2021)
    print(f"Part 1: {d9p1(lines)}")
    print(f"Part 2: {d9p2(lines)}")
