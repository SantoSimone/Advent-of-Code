import collections
import queue
from typing import List, Dict, Tuple

import python_utils

PIPES = {
    # (x, y) of prev and next neigh
    "|": ((0, -1), (0, +1)),
    "-": ((-1, 0), (1, 0)),
    "L": ((0, -1), (1, 0)),
    "J": ((0, -1), (-1, 0)),
    "7": ((-1, 0), (0, 1)),
    "F": ((0, 1), (1, 0)),
    "S": None
}


def parse_grid(lines: List[str]):
    # x grows to the right, y grows down
    grid = collections.defaultdict(lambda: ())
    start_pos = None
    for j, line in enumerate(lines):
        for i, c in enumerate(line):
            if c == '.':
                continue
            elif c == "S":
                start_pos = (i, j)

            grid[i, j] = PIPES[c]

    return grid, start_pos


def get_neigh(pos: Tuple[int, int], grid: Dict[Tuple[int, int], Tuple[Tuple[int, int], Tuple[int, int]]]):
    neighbors = []
    for i, j in grid[pos]:
        if pos[0] + i < 0 or pos[1] + j < 0:
            continue
        neighbors.append((pos[0] + i, pos[1] + j))

    return neighbors


def find_loop(start_pos: Tuple[int, int], grid: Dict[Tuple[int, int], Tuple[Tuple[int, int], Tuple[int, int]]]):
    visited = {start_pos}
    distances = {start_pos: 0}

    to_visit = queue.PriorityQueue()
    for neigh in get_neigh(start_pos, grid):
        to_visit.put((1, neigh))

    while not to_visit.empty():
        curr_steps, curr_pos = to_visit.get()
        if curr_pos in visited:
            break

        visited.add(curr_pos)
        distances[curr_pos] = curr_steps
        for neigh in get_neigh(curr_pos, grid):
            if neigh in visited:
                continue
            to_visit.put((curr_steps + 1, neigh))

    return distances, curr_pos


def find_start_pipe(start_pos: Tuple[int, int], grid: Dict) -> Tuple[int, int]:
    x, y = start_pos
    possible_connections = []
    for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        connections = grid[x + i, y + j]
        for ii, jj in connections:
            if -ii == i and -jj == j:
                possible_connections.append((i, j))

    # Otherwise we would have to combine each possible connections and try many possible starting pipes
    assert len(possible_connections) == 2

    return next(v for v in PIPES.values() if v is not None and all(c in v for c in possible_connections))


def d10p1(lines: List[str]):
    grid, start_pos = parse_grid(lines)
    grid[start_pos] = find_start_pipe(start_pos, grid)
    distances, loop_pos = find_loop(start_pos, grid)

    return max(v for v in distances.values())


def get_vertices(start_pos: Tuple[int, int], grid):
    to_visit = [start_pos]
    visited = {start_pos}
    vertices = []
    vertices_neighbors = {v for k, v in PIPES.items() if k in 'JFL7'}
    while len(to_visit) > 0:
        curr_pos = to_visit.pop()
        if grid[curr_pos] in vertices_neighbors:
            if curr_pos in vertices:
                break
            vertices.append(curr_pos)

        visited.add(curr_pos)
        for neigh in get_neigh(curr_pos, grid):
            if neigh in visited:
                continue
            to_visit.append(neigh)

    return vertices


def area_and_perimeter(vertices: List[Tuple[int, int]]) -> Tuple[int, int]:
    # Vertices should be in the form (y, x)
    # Area is defined as the summation in i of curr_y * (prev_x - next_x) / 2
    n = len(vertices)
    area = 0
    perimeter = 0
    for i, (curr_y, curr_x) in enumerate(vertices):
        next_y, next_x = vertices[(i + 1) % n]
        perimeter += abs(curr_x - next_x) + abs(curr_y - next_y)
        area += (curr_y + next_y) * (next_x - curr_x)

    return abs(area) // 2, perimeter


def d10p2(lines: List[str]):
    grid, start_pos = parse_grid(lines)
    grid[start_pos] = find_start_pipe(start_pos, grid)
    distances, loop_pos = find_loop(start_pos, grid)
    vertices = get_vertices(loop_pos, grid)
    area, perimeter = area_and_perimeter(vertices)

    return area - perimeter // 2 + 1


if __name__ == '__main__':
    day, year = 10, 2023
    lines = python_utils.get_input_as_lines(day, year)
    print(f'Part 1: {d10p1(lines)}')
    print(f'Part 2: {d10p2(lines)}')
