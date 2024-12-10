import collections
from typing import List

import python_utils


def d10p1(lines: List[str]):
    # Straight compute all possible trails and keep track of unique 9-height final positions for each starting point

    grid = {
        (i, j): int(c)
        for i, line in enumerate(lines)
        for j, c in enumerate(line)
    }

    q = [[(i, j)] for (i, j), c in grid.items() if c == 0]
    sols = collections.defaultdict(set)
    while q:
        path = q.pop()
        curr = path[-1]

        curr_height = grid[curr]
        if curr_height == 9:
            sols[path[0]].add(path[-1])

        for neigh in python_utils.grid_neighbors(curr):
            if neigh in grid and grid[neigh] == curr_height + 1:
                q.append(path + [neigh])

    return sum(map(len, sols.values()))


def d10p2(lines: List[str]):
    # Remove the uniqueness constraint on the solution :D

    grid = {
        (i, j): int(c)
        for i, line in enumerate(lines)
        for j, c in enumerate(line)
    }

    q = [[(i, j)] for (i, j), c in grid.items() if c == 0]
    sols = collections.defaultdict(int)
    while q:
        path = q.pop()
        curr = path[-1]

        curr_height = grid[curr]
        if curr_height == 9:
            sols[path[0]] += 1

        for neigh in python_utils.grid_neighbors(curr):
            if neigh in grid and grid[neigh] == curr_height + 1:
                q.append(path + [neigh])

    return sum(sols.values())


if __name__ == '__main__':
    day, year = 10, 2024
    lines = python_utils.get_input_as_lines(day, year)
    print(f'Part 1: {d10p1(lines)}')
    print(f'Part 2: {d10p2(lines)}')
