import collections
from typing import List

import python_utils

DIR = [
    [-1, 0],  # up
    [0, 1],  # right
    [1, 0],  # down
    [0, -1],  # left
]


def d22p1(lines: List[str]):
    grid = collections.defaultdict(bool, {
        (i, j): c == "#"
        for i, line in enumerate(lines)
        for j, c in enumerate(line)
    })
    pos = (len(lines) // 2, len(lines[0]) // 2)
    idx_dir = 0
    infected = 0
    for _ in range(10_000):
        # Update dir
        idx_dir += 1 if grid[pos] else -1
        idx_dir = idx_dir % 4

        # Change grid val
        grid[pos] = not grid[pos]

        # Update counter
        if grid[pos]:
            infected += 1

        # Update pos
        pos = (pos[0] + DIR[idx_dir][0], pos[1] + DIR[idx_dir][1])

    return infected


def d22p2(lines: List[str]):
    grid = collections.defaultdict(int, {
        (i, j): 2 if c == "#" else 0
        for i, line in enumerate(lines)
        for j, c in enumerate(line)
    })
    pos = (len(lines) // 2, len(lines[0]) // 2)
    idx_dir = 0
    infected = 0
    for _ in range(10_000_000):
        # Update dir (in the worst way python allows it)
        idx_dir += -1 if grid[pos] == 0 else 0 if grid[pos] == 1 else 1 if grid[pos] == 2 else 2
        idx_dir = idx_dir % 4

        # Change grid val
        grid[pos] = (grid[pos] + 1) % 4

        # Update counter
        if grid[pos] == 2:
            infected += 1

        # Update pos
        pos = (pos[0] + DIR[idx_dir][0], pos[1] + DIR[idx_dir][1])

    return infected


if __name__ == '__main__':
    day, year = 22, 2017
    lines = python_utils.get_input_as_lines(day, year)
    print(f'Part 1: {d22p1(lines)}')
    print(f'Part 2: {d22p2(lines)}')
