import queue
from typing import List, Dict, Tuple

import python_utils


def parse_starting_grid(lines: List[str]):
    grid_h = grid_w = 71
    num_bytes = 1024
    grid = {
        (y, x): True
        for y in range(grid_h)
        for x in range(grid_w)
    }
    for x, y in map(python_utils.parse_ints, lines[:num_bytes]):
        grid[y, x] = False

    return grid


def find_best_path(grid: Dict[Tuple[int, int], bool]):
    pos = (0, 0)
    target = max(grid.keys())
    q = queue.PriorityQueue()
    q.put((0, pos, []))
    visited = set()
    while not q.empty():
        steps, pos, path = q.get()
        if pos in visited:
            continue

        visited.add(pos)
        if pos == target:
            return path

        for neigh in python_utils.grid_neighbors(pos):
            if neigh in grid and grid[neigh]:
                q.put((steps + 1, neigh, path + [neigh]))

    return None


def d18p1(lines: List[str]):
    # Simple BFS through the grid

    grid = parse_starting_grid(lines)
    return len(find_best_path(grid))


def d18p2(lines: List[str]):
    # Brute force seems tractable, but with some minor tricks to avoid completely brute-forcing the problem
    # i) start after the first 1024 bytes as the problem is solvable at 1024
    # ii) if the next corrupted byte is not in the current best path, skip it

    grid = parse_starting_grid(lines)
    best_path = find_best_path(grid)

    for x, y in map(python_utils.parse_ints, lines[1024:]):
        grid[y, x] = False
        if (y, x) in best_path:
            best_path = find_best_path(grid)
            if best_path is None:
                return x, y

    return None


if __name__ == '__main__':
    day, year = 18, 2024
    lines = python_utils.get_input_as_lines(day, year)
    print(f'Part 1: {d18p1(lines)}')
    print(f'Part 2: {d18p2(lines)}')
