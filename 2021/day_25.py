from typing import List, Dict
from python_utils import get_input_as_lines, splitter


class Occupancy:
    VOID = 0
    EAST = 1
    SOUTH = 2


def check_moves(grid: Dict, h: int, w: int, type: Occupancy) -> List:
    moves = []
    for (i, j), x in grid.items():
        if x == type == Occupancy.SOUTH and grid[((i + 1) % h, j)] == Occupancy.VOID:
            moves.append((i, j, Occupancy.SOUTH))
        elif x == type == Occupancy.EAST and grid[(i, (j + 1) % w)] == Occupancy.VOID:
            moves.append((i, j, Occupancy.EAST))

    return moves


def perform_moves(grid: Dict, h: int, w: int, moves: List) -> Dict:
    tmp = grid.copy()
    for i, j, type in moves:
        tmp[(i, j)] = Occupancy.VOID
        if type == Occupancy.SOUTH:
            tmp[((i + 1) % h, j)] = Occupancy.SOUTH
        else:
            tmp[(i, (j + 1) % w)] = Occupancy.EAST

    return tmp


def print_grid(grid, h, w):
    print('--------------------')
    for i in range(h):
        for j in range(w):
            c = '>' if grid[i, j] == Occupancy.EAST else 'v' if grid[i, j] == Occupancy.SOUTH else '.'
            print(c, end='')
        print("")


def d25p1(lines: List[str]):
    h = len(lines)
    w = len(lines[0])
    grid = {}
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            grid[i, j] = Occupancy.EAST if c == '>' else Occupancy.SOUTH if c == 'v' else Occupancy.VOID

    step = 1
    # print_grid(grid, h, w)
    while True:
        moving_east = check_moves(grid, h, w, Occupancy.EAST)

        grid = perform_moves(grid, h, w, moving_east)
        moving_south = check_moves(grid, h, w, Occupancy.SOUTH)
        if len(moving_east) < 1 and len(moving_south) < 1:
            break

        grid = perform_moves(grid, h, w, moving_south)
        step += 1
        # print_grid(grid, h, w)

    return step


if __name__ == '__main__':
    lines = get_input_as_lines(25, 2021)
    print(f"Part 1: {d25p1(lines)}")
