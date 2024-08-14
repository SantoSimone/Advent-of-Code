import collections
from typing import List

import python_utils


def parse_input(lines: List[str]):
    grid = {(i, j): 1 if c == '#' else 0
            for i, line in enumerate(lines)
            for j, c in enumerate(line)}
    start_pos = next((i, j) for i, line in enumerate(lines) for j, c in enumerate(line) if c == 'S')

    return grid, start_pos


def walk_grid(start_pos, grid, max_steps):
    visited = set()
    queue = collections.deque([(0, start_pos)])
    h = w = len(grid)

    result = 0
    while queue:
        dist, pos = queue.popleft()

        if pos in visited:
            continue

        visited.add(pos)

        if dist % 2 == max_steps % 2:
            # This path can be reached in the specified number of steps
            result += 1

        if dist >= max_steps:
            continue

        y, x = pos
        for i, j in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            new_y = (y + i) % h
            new_x = (x + j) % w
            if grid.get((new_y, new_x), 1) == 0:
                queue.append((dist + 1, (new_y, new_x)))

    return result


def d21p1(lines: List[str]):
    grid, start_pos = parse_input(lines)
    sol = walk_grid(start_pos, grid, 64)
    return sol


#
# def d21p2(lines: List[str]):
#     # This part wanted us to look into the input and find a "shortcut", I hate this kind of days.
#     # Credits to https://github.com/WinslowJosiah/adventofcode/blob/main/aoc2023/day21/__init__.py
#     # for the interesting visual explanation
#
#     grid, start_pos = parse_input(lines)
#     w = len(grid)
#     n = 26501365 // w
#     a, b, c = (
#         walk_grid(start_pos, grid, s * w + (w // 2))
#         for s in range(3)
#     )
#     return a + n * (b - a + (n - 1) * (c - b - b + a) // 2)

def d21p2(lines: List[str]):
    # I hate this kind of days in which you have to hack the input data, solution is extracted from reddit megathread

    grid = [list(row) for row in lines]
    m, n = len(grid), len(grid[0])

    x_final, remainder = divmod(26_501_365, n)
    border_crossings = [remainder, remainder + n, remainder + 2 * n]

    visited = set()
    queue = collections.deque([(n // 2, n // 2)])
    total = [0, 0]  # [even, odd]
    Y = []
    for step in range(1, border_crossings[-1] + 1):
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for i, j in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if (i, j) in visited or grid[i % m][j % n] == '#':
                    continue

                visited.add((i, j))
                queue.append((i, j))
                total[step % 2] += 1

        if step in border_crossings:
            Y.append(total[step % 2])

    import numpy as np
    X = [0, 1, 2]
    coefficients = np.polyfit(X, Y, deg=2)  # get coefficients for quadratic equation y = a*x^2 + bx + c
    y_final = np.polyval(coefficients, x_final)  # using coefficients, get y value at x_final
    return y_final.round().astype(int)


if __name__ == '__main__':
    day, year = 21, 2023
    lines = python_utils.get_input_as_lines(day, year)
    print(f'Part 1: {d21p1(lines)}')
    print(f'Part 2: {d21p2(lines)}')
