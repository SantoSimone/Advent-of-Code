import functools
from typing import List

import numpy as np

import python_utils


def get_matrices(lines: List[str]):
    grids = python_utils.splitter(lines, '')
    matrices = []
    for grid in grids:
        matrix = np.zeros((len(grid), len(grid[0])), dtype=int)
        for i, line in enumerate(grid):
            for j, c in enumerate(line):
                matrix[i, j] = 1 if c == "#" else 0
        matrices.append(matrix)

    return matrices


def get_reflection(matrix: np.ndarray, diffs: int):
    # First we try over rows
    for num_rows in range(1, matrix.shape[0] // 2 + 1):
        if np.sum(matrix[:num_rows] != np.flip(matrix[num_rows:num_rows * 2], axis=0)) == diffs:
            return num_rows * 100
        if np.sum(matrix[-num_rows:] != np.flip(matrix[-num_rows * 2:-num_rows], axis=0)) == diffs:
            return (matrix.shape[0] - num_rows) * 100

    # then we try over cols
    for num_cols in range(1, matrix.shape[1] // 2 + 1):
        if np.sum(matrix[:, :num_cols] != np.flip(matrix[:, num_cols:num_cols * 2], axis=1)) == diffs:
            return num_cols
        if np.sum(matrix[:, -num_cols:] != np.flip(matrix[:, -num_cols * 2:-num_cols], axis=1)) == diffs:
            return matrix.shape[1] - num_cols


def d13p1(lines: List[str]):
    # Not much time today, gonna write awful code :)
    # Maybe coming back during holidays
    matrices = get_matrices(lines)
    func = functools.partial(get_reflection, diffs=0)
    reflections = map(func, matrices)
    return sum(reflections)


def d13p2(lines: List[str]):
    matrices = get_matrices(lines)
    func = functools.partial(get_reflection, diffs=1)
    reflections = map(func, matrices)
    return sum(reflections)


if __name__ == '__main__':
    day, year = 13, 2023
    lines = python_utils.get_input_as_lines(day, year)
    print(f'Part 1: {d13p1(lines)}')
    print(f'Part 2: {d13p2(lines)}')
