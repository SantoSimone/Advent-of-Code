from typing import List, Tuple

import numpy as np

import python_utils


def parse_grid(lines: List[str]):
    grid = np.zeros((len(lines), len(lines[0])))
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == '#':
                grid[i, j] = 1
            elif c == 'O':
                grid[i, j] = 2

    return grid


def tilt_grid(grid: np.ndarray, rock_positions: List[Tuple[int, int]], direction: Tuple[int, int]):
    move_y, move_x = direction

    def can_move(p_y, p_x):
        return (0 <= p_y + move_y < grid.shape[0] and
                0 <= p_x + move_x < grid.shape[1] and
                grid[p_y + move_y, p_x + move_x] == 0)

    for pos in rock_positions:
        y, x = pos
        grid[y, x] = 0
        while can_move(y, x):
            y += move_y
            x += move_x
        grid[y, x] = 2

    return grid


def d14p1(lines: List[str]):
    # Core function has been already refactored for part 2 solution
    grid = parse_grid(lines)
    tilt_grid(grid, list(zip(*np.where(grid == 2))), (-1, 0))
    count_by_line = [np.sum(grid[i] == 2) for i in range(grid.shape[0])]
    load_by_line = [(len(count_by_line) - i) * val for i, val in enumerate(count_by_line)]
    return sum(load_by_line)


def d14p2(lines: List[str]):
    # Assume there must be a loop of states, find it and skip as many cycles as we can
    grid = parse_grid(lines)
    moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    visited = [list(zip(*np.where(grid == 2)))]
    cycles = 0
    loop_start = None
    while cycles < 1_000_000_000:
        for i in range(4):
            positions = list(zip(*np.where(grid == 2)))
            if i == 2:
                positions = sorted(positions, key=lambda p: p[0], reverse=True)
            if i == 3:
                positions = sorted(positions, key=lambda p: p[1], reverse=True)
            tilt_grid(grid, positions, moves[i])

        curr = list(zip(*np.where(grid == 2)))
        cycles += 1
        if curr in visited and loop_start is None:
            loop_start = visited.index(curr)
            loop_size = cycles - loop_start
            remaining = 1_000_000_000 - loop_start
            skips = (remaining // loop_size) * loop_size
            cycles = loop_start + skips
        else:
            visited.append(curr)

    count_by_line = [np.sum(grid[i] == 2) for i in range(grid.shape[0])]
    load_by_line = [(len(count_by_line) - i) * val for i, val in enumerate(count_by_line)]
    return sum(load_by_line)


if __name__ == '__main__':
    day, year = 14, 2023
    lines = python_utils.get_input_as_lines(day, year)
    print(f'Part 1: {d14p1(lines)}')
    print(f'Part 2: {d14p2(lines)}')
