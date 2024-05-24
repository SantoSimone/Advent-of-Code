from collections import defaultdict, Counter
from typing import List

import python_utils

# Not in the right mood for clean code today :)
CHECKS = {
    0: [(-1, -1), (-1, 0), (-1, 1)],  # North
    1: [(1, -1), (1, 0), (1, 1)],  # South
    2: [(-1, -1), (0, -1), (1, -1)],  # West
    3: [(-1, 1), (0, 1), (1, 1)],  # East
}
grid = defaultdict(int)


def next_move(r, c, pref):
    neighbors = 0
    for i in range(4):
        neighbors += sum(grid[r + add_r, c + add_c] for add_r, add_c in CHECKS[i])

    if neighbors == 0:
        return r, c

    for i in range(4):
        facing = (pref + i) % 4
        if all(grid[r + add_r, c + add_c] == 0 for add_r, add_c in CHECKS[facing]):
            return r + CHECKS[facing][1][0], c + CHECKS[facing][1][1]

    return r, c


def d23p1(lines: List[str]):
    global grid
    for r, line in enumerate(lines):
        for c, char in enumerate(line):
            grid[r, c] = 1 if char == '#' else 0

    for pref in range(10):
        to_eval = [(r, c) for r, c in grid.keys() if grid[r, c] == 1]
        proposals = {
            (r, c): next_move(r, c, pref % 4)
            for r, c in to_eval
        }
        counter = Counter(proposals.values())
        for r, c in to_eval:
            r_new, c_new = proposals[r, c]
            if counter[r_new, c_new] == 1:
                grid[r, c] = 0
                grid[r_new, c_new] = 1

    min_r = min([r for r, c in grid.keys() if grid[r, c] == 1])
    max_r = max([r for r, c in grid.keys() if grid[r, c] == 1])
    min_c = min([c for r, c in grid.keys() if grid[r, c] == 1])
    max_c = max([c for r, c in grid.keys() if grid[r, c] == 1])
    tot = 0
    for row in range(min_r, max_r + 1):
        for col in range(min_c, max_c + 1):
            tot += 1 if grid[row, col] == 0 else 0

    return tot


def d23p2(lines: List[str]):
    global grid
    grid = defaultdict(int)
    for r, line in enumerate(lines):
        for c, char in enumerate(line):
            grid[r, c] = 1 if char == '#' else 0

    pref = 0
    while True:
        to_eval = [(r, c) for r, c in grid.keys() if grid[r, c] == 1]
        proposals = {
            (r, c): next_move(r, c, pref % 4)
            for r, c in to_eval
        }
        counter = Counter(proposals.values())
        moved = False
        for r, c in to_eval:
            r_new, c_new = proposals[r, c]
            if counter[r_new, c_new] == 1:
                if r_new != r or c_new != c:
                    moved = True
                grid[r, c] = 0
                grid[r_new, c_new] = 1

        pref += 1
        if not moved:
            break

    return pref


if __name__ == '__main__':
    lines = python_utils.get_input_as_lines(23, 2022)
    print(f"Part 1: {d23p1(lines)}")
    print(f"Part 2: {d23p2(lines)}")
