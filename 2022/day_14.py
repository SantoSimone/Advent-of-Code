from typing import List

import numpy as np

import python_utils


def create_grid(lines: List[str]):
    grid = np.zeros((1000, 1000))

    for line in lines:
        coords = [python_utils.parse_ints(x) for x in line.split('->')]
        for i, coord1 in enumerate(coords[:-1]):
            c1, r1 = coord1
            c2, r2 = coords[i + 1]
            grid[min(r1, r2):max(r1, r2) + 1, min(c1, c2):max(c1, c2) + 1] = 1

    return grid


def d14p1(lines: List[str]):
    grid = create_grid(lines)
    rs, cs = 0, 500
    count = 0
    while True:
        movements = [(1, 0), (1, -1), (1, 1)]
        if grid[rs:, cs].sum() < 1:
            return count
        if all(grid[rs + rm, cs + cm] for rm, cm in movements):
            grid[rs, cs] = 1
            count += 1
            rs, cs = 0, 500
            continue

        for rm, cm in movements:
            if grid[rs + rm, cs + cm] == 0:
                rs, cs = rs + rm, cs + cm
                break


def d14p2(lines: List[str]):
    grid = create_grid(lines)
    last_y = np.max(np.nonzero(np.sum(grid, axis=1)))
    grid[last_y + 2] = 1
    rs, cs = 0, 500
    count = 0
    moves = 0
    while True:
        movements = [(1, 0), (1, -1), (1, 1)]
        if all(grid[rs + rm, cs + cm] for rm, cm in movements):
            if moves == 0:
                return count + 1
            moves = 0
            grid[rs, cs] = 1
            count += 1
            rs, cs = 0, 500
            continue

        for rm, cm in movements:
            if grid[rs + rm, cs + cm] == 0:
                rs, cs = rs + rm, cs + cm
                moves += 1
                break


if __name__ == '__main__':
    lines = python_utils.get_input_as_lines(14, 2022)
    print(f"Part 1: {d14p1(lines)}")
    print(f"Part 2: {d14p2(lines)}")
