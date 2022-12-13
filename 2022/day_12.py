import functools
import itertools
import operator
import queue
import re
from collections import deque
from typing import List

import numpy as np

import python_utils


def d12p1(lines: List[str]):
    # Comment for the future me: you definitely need an hackpack with BFS, DFS, A*, etc
    grid = np.zeros(shape=(len(lines), len(lines[0])), dtype=np.int32)
    start_pos = (0, 0)
    end_pos = (0, 0)
    for i, line in enumerate(lines):
        row = [ord(x) - ord('a') for x in line]
        grid[i] = np.array(row)

        p = line.find('S')
        if p != -1:
            start_pos = (i, p)
            grid[i, p] = 0
        p = line.find('E')
        if p != -1:
            end_pos = (i, p)
            grid[i, p] = ord('z') - ord('a')

    # Every element of the queue will be: number of steps, distance from the end, visited positions, current position
    q = deque()
    q.append((0, start_pos))
    h, w = grid.shape
    visited = set()
    while q:
        dist, (r, c) = q.popleft()
        if (r, c) == end_pos:
            return dist

        neighbors = [(r + i, c + j) for (i, j) in [(-1, 0), (1, 0), (0, -1), (0, 1)]]
        if (r, c) not in visited:
            visited.add((r, c))
            for (new_r, new_c) in neighbors:
                if 0 <= new_r < h and 0 <= new_c < w:
                    if grid[new_r, new_c] > grid[r, c] + 1 or (new_r, new_c) in visited:
                        continue
                    q.append((dist + 1, (new_r, new_c)))

    return -1


def d12p2(lines: List[str]):
    grid = np.zeros(shape=(len(lines), len(lines[0])), dtype=np.int32)
    end_pos = (0, 0)
    for i, line in enumerate(lines):
        row = [ord(x) - ord('a') for x in line]
        grid[i] = np.array(row)

        p = line.find('E')
        if p != -1:
            end_pos = (i, p)
            grid[i, p] = ord('z') - ord('a')

    # Every element of the queue will be: number of steps, distance from the end, visited positions, current position
    best = 383  # first part result
    h, w = grid.shape
    for i, j in np.argwhere(grid == 0):
        q = deque()
        q.append((0, (i, j)))
        visited = set()
        solved = False
        dist = best
        while q:
            dist, (r, c) = q.popleft()
            if (r, c) == end_pos:
                solved = True
                break

            neighbors = [(r + i, c + j) for (i, j) in [(-1, 0), (1, 0), (0, -1), (0, 1)]]
            if (r, c) not in visited:
                visited.add((r, c))
                for (new_r, new_c) in neighbors:
                    if 0 <= new_r < h and 0 <= new_c < w:
                        if grid[new_r, new_c] > grid[r, c] + 1 or (new_r, new_c) in visited:
                            continue
                        q.append((dist + 1, (new_r, new_c)))

        if solved and dist < best:
            best = dist
    return best


if __name__ == '__main__':
    lines = python_utils.get_input_as_lines(12, 2022)
    print(f"Part 1: {d12p1(lines)}")
    print(f"Part 2: {d12p2(lines)}")
