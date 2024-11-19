from typing import List

import numpy as np

import python_utils


def d10(lines: List[str]):
    points = np.array([python_utils.parse_ints(line) for line in lines])

    closest, closest_size, step = None, 1e20, 0
    for i in range(1, 100_000):
        points[:, :2] += points[:, 2:4]
        min_x = points[:, 0].min()
        max_x = points[:, 0].max()
        min_y = points[:, 1].min()
        max_y = points[:, 1].max()

        if (max_x - min_x) * (max_y - min_y) < closest_size:
            closest = points.copy()
            closest_size = (max_x - min_x) * (max_y - min_y)
            step = i

    min_x = closest[:, 0].min()
    max_x = closest[:, 0].max()
    min_y = closest[:, 1].min()
    max_y = closest[:, 1].max()

    grid = np.zeros(shape=(max_y - min_y + 1, max_x - min_x + 1), dtype=bool)
    for x, y in closest[:, :2]:
        grid[y - min_y, x - min_x] = True

    closest = '\n'.join([
        ''.join(['#' if p else '.' for p in grid[y]])
        for y in range(grid.shape[0])
    ])

    return '\n' + closest, step


if __name__ == '__main__':
    day, year = 10, 2018
    lines = python_utils.get_input_as_lines(day, year)
    p1, p2 = d10(lines)
    print(f'Part 1: {p1}')
    print(f'Part 2: {p2}')
