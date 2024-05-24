import collections
from typing import List, Tuple, Dict

import python_utils

# (y, x)
MOVES = [(0, 1), (1, 0), (0, -1), (-1, 0)]

INTERACTIONS = {
    # 0 right
    0: {"/": [3], "\\": [1], "|": [1, 3], "-": [0]},

    # 1 down
    1: {"/": [2], "\\": [0], "|": [1], "-": [0, 2]},

    # 2 left
    2: {"/": [1], "\\": [3], "|": [1, 3], "-": [2]},

    # 3 up
    3: {"/": [0], "\\": [2], "|": [3], "-": [0, 2]},
}


def parse_grid(lines: List[str]) -> Tuple[Dict[Tuple[int, int], str], int, int]:
    grid = {}
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            grid[i, j] = c

    return grid, len(lines), len(lines[0])


def count_energized_tiles(grid: Dict[Tuple[int, int], str], h: int, w: int, start_beam: Tuple[int, int, int]) -> int:
    beams = [start_beam]
    interaction_chars = INTERACTIONS[0].keys()
    visited = collections.defaultdict(set)
    while beams:
        dir_idx, y, x = beams.pop()
        # Out of grid
        if not (0 <= y < h and 0 <= x < w):
            continue
        # Detected loop
        if dir_idx in visited[y, x]:
            continue
        visited[y, x].add(dir_idx)
        curr_char = grid[y, x]
        if curr_char in interaction_chars:
            for new_dir_idx in INTERACTIONS[dir_idx][curr_char]:
                dir_y, dir_x = MOVES[new_dir_idx]
                beams.append((new_dir_idx, y + dir_y, x + dir_x))
        else:
            dir_y, dir_x = MOVES[dir_idx]
            beams.append((dir_idx, y + dir_y, x + dir_x))

    return len(visited)


def d16p1(lines: List[str]):
    grid, h, w = parse_grid(lines)
    return count_energized_tiles(grid, h, w, (0, 0, 0))


def d16p2(lines: List[str]):
    grid, h, w = parse_grid(lines)
    max_energy = 0
    for i in range(h):
        # Test leftmost column heading right
        energy = count_energized_tiles(grid, h, w, (0, i, 0))
        if energy > max_energy:
            max_energy = energy
        # Test rightmost column heading left
        energy = count_energized_tiles(grid, h, w, (2, i, w - 1))
        if energy > max_energy:
            max_energy = energy

    for j in range(w):
        # Test top row heading down
        energy = count_energized_tiles(grid, h, w, (1, 0, j))
        if energy > max_energy:
            max_energy = energy
        # Test bottom row heading up
        energy = count_energized_tiles(grid, h, w, (3, h - 1, j))
        if energy > max_energy:
            max_energy = energy

    return max_energy


if __name__ == '__main__':
    day, year = 16, 2023
    lines = python_utils.get_input_as_lines(day, year)
    print(f'Part 1: {d16p1(lines)}')
    print(f'Part 2: {d16p2(lines)}')
