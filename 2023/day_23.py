import collections
from typing import List, Tuple, Dict, Set

import python_utils

MOVES = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def parse_grid(lines: List[str]) -> Dict[Tuple[int, int], int]:
    grid = {}
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == '#':
                val = 0
            elif c == '.':
                val = 1
            elif c == '>':
                val = 2
            elif c == '<':
                val = 3
            elif c == 'v':
                val = 4
            else:  # c == '^':
                val = 5

            grid[i, j] = val

    return grid


def d23p1(lines: List[str]):
    grid = parse_grid(lines)

    pos = next(k for k, v in grid.items() if k[0] == 0 and v == 1)
    last_row = max(grid, key=lambda k: k[0])[0]
    positions = collections.deque([(pos, set())])
    res = []
    while positions:
        pos, visited = positions.popleft()

        if pos in visited:
            continue

        if pos[0] == last_row:
            res.append(len(visited))
            continue

        curr_val = grid.get(pos, 0)
        if curr_val == 0:
            continue
        elif curr_val == 1:
            next_moves = MOVES
        else:  # grid[pos] > 1:
            next_moves = [MOVES[curr_val - 2]]

        y, x = pos
        for add_y, add_x in next_moves:
            curr_visited = visited.copy()
            curr_visited.add(pos)
            positions.append(((y + add_y, x + add_x), curr_visited))

    return max(res)


def compress_grid(grid: Dict[Tuple[int, int], int]) \
        -> Dict[Tuple[int, int], List[Tuple[Tuple[int, int], Set[Tuple[int, int]]]]]:
    """Find 'waypoints', i.e. crosses where next step is not forced by the grid structure, and save a compressed version
     of the grid, where neighbors of a point are the next waypoints reachable from that waypoint  """

    def neighbors(y, x):
        return [(y + add_y, x + add_x) for add_y, add_x in MOVES if grid.get((y + add_y, x + add_x), 0) != 0]

    first_pos = next(k for k, v in grid.items() if k[0] == 0 and v == 1)

    waypoints = [first_pos] + [
        (y, x)
        for (y, x), v in grid.items()
        if grid[y, x] != 0 and len(neighbors(y, x)) > 2
    ]

    waypoint_neighbors = collections.defaultdict(list)
    last_row = max(grid, key=lambda k: k[0])[0]
    last_point = next(k for k, v in grid.items() if k[0] == last_row and v == 1)
    for way in waypoints:
        seen = set()
        seen.add(way)
        positions = collections.deque([(neigh, 1) for neigh in neighbors(*way)])
        while positions:
            pos, dist = positions.popleft()
            if pos in seen:
                continue
            seen.add(pos)
            if pos in waypoints or pos == last_point:
                waypoint_neighbors[way].append((pos, dist))
                continue

            for neigh in neighbors(*pos):
                positions.append((neigh, dist + 1))

    return waypoint_neighbors


def d23p2(lines: List[str]):
    # First compress the grid, by removing all points where the path is mandatory (you can only move either "ahead"
    # or "backward")
    grid = parse_grid(lines)
    compressed_grid = compress_grid(grid)

    first_pos = next(k for k, v in grid.items() if k[0] == 0 and v == 1)
    last_row = max(grid, key=lambda k: k[0])[0]
    positions = collections.deque([(first_pos, set(), 0)])
    res = []
    while positions:
        pos, visited, dist = positions.popleft()

        if pos[0] == last_row:
            res.append(dist)
            continue

        curr_visited = visited.copy()
        curr_visited.add(pos)
        for neigh, add_dist in compressed_grid[pos]:
            if neigh in curr_visited:
                continue
            positions.append((neigh, curr_visited, dist + add_dist))

    return max(res)


if __name__ == '__main__':
    day, year = 23, 2023
    lines = python_utils.get_input_as_lines(day, year)
    print(f'Part 1: {d23p1(lines)}')
    print(f'Part 2: {d23p2(lines)}')
