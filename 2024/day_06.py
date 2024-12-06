from typing import List, Tuple, Dict

import python_utils

# down, left, up, right - looping through this array we always turn right
DIRS = [(1, 0), (0, -1), (-1, 0), (0, 1)]


def parse_input(lines: List[str]) -> Tuple[Dict[Tuple[int, int], bool], Tuple[int, int], int]:
    # Input grid is created so that '.' -> True, otherwise False
    grid = {}
    pos = dir_idx = None
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c in ['v', '^', '<', '>']:
                pos = (i, j)
                dir_idx = ['v', '<', '^', '>'].index(c)
                c = '.'

            grid[i, j] = c == '.'

    return grid, pos, dir_idx


def step(grid: Dict[Tuple[int, int], bool], pos: Tuple[int, int], dir_idx: int):
    y, x = pos
    dir_y, dir_x = DIRS[dir_idx]
    if not grid.get((y + dir_y, x + dir_x), True):
        dir_idx = (dir_idx + 1) % len(DIRS)
    else:
        pos = (y + dir_y, x + dir_x)

    return dir_idx, pos


def d6p1(lines: List[str]):
    # Simple instructions, not much to say. I just created some function to be reused in part 2

    grid, pos, dir_idx = parse_input(lines)
    visited = set()
    while pos in grid:
        visited.add(pos)
        dir_idx, pos = step(grid, pos, dir_idx)

    return len(visited)


def check_loop(grid: Dict[Tuple[int, int], bool], pos: Tuple[int, int], dir_idx: int) -> bool:
    visited = set()
    while pos in grid:
        if (pos, dir_idx) in visited:
            return True

        visited.add((pos, dir_idx))
        dir_idx, pos = step(grid, pos, dir_idx)

    return False


def d6p2(lines: List[str]):
    # Find all position of part 1, then try putting an obstacle in each of them
    
    grid, start_pos, start_dir_idx = parse_input(lines)
    possible_obstacles = set()
    pos = start_pos
    dir_idx = start_dir_idx
    while pos in grid:
        possible_obstacles.add(pos)
        dir_idx, pos = step(grid, pos, dir_idx)

    possible_obstacles.remove(start_pos)
    loops = set()
    for obstacle in possible_obstacles:
        new_grid = grid.copy()
        new_grid[obstacle] = False
        if check_loop(new_grid, start_pos, start_dir_idx):
            loops.add(obstacle)

    return len(loops)


if __name__ == '__main__':
    day, year = 6, 2024
    lines = python_utils.get_input_as_lines(day, year)
    print(f'Part 1: {d6p1(lines)}')
    print(f'Part 2: {d6p2(lines)}')
