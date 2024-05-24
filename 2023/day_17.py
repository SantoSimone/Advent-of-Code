import queue
from typing import List

import python_utils

# (y, x)
MOVES = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def parse_grid(lines: List[str]):
    grid = {
        (i, j): int(c)
        for i, line in enumerate(lines)
        for j, c in enumerate(line)
    }

    return grid


def d17p1(lines: List[str]):
    # Strange pathfinding, will implement step by step for both parts
    grid = parse_grid(lines)
    h, w = len(lines), len(lines[0])

    # Priority queue for cell to check - each cell is
    # (sum of heat loss, y, x, direction, num of moves in current direction, path)
    # directions: 0 right, 1 down, 2 left, 3 up
    # Note: we store path only for debugging purposes
    q = queue.PriorityQueue()
    q.put((-grid[0, 0], 0, 0, 0, 0, []))
    visited = set()
    while q:
        curr_sum, y, x, direction, moves_in_curr_dir, path = q.get()

        # Out of grid
        if not (0 <= y < h and 0 <= x < w):
            continue

        # Finish
        if y == h - 1 and x == w - 1:
            return curr_sum + grid[y, x]

        # Do not compute again position we already reached with the same pathing conditions
        if (y, x, direction, moves_in_curr_dir) in visited:
            continue
        visited.add((y, x, direction, moves_in_curr_dir))

        # Previous and next moves are 90-degree by construction of `MOVES` list, we always consider those as candidates
        # for next direction
        next_possible_dir = [(direction - 1) % 4, (direction + 1) % 4]
        # If we did not move more than 3 steps, we can also consider current direction as next direction
        if moves_in_curr_dir < 3:
            next_possible_dir.append(direction)

        # Fill the queue with the new candidates
        for next_dir in next_possible_dir:
            dir_y, dir_x = MOVES[next_dir]
            q.put((
                curr_sum + grid[y, x],  # total heat loss
                y + dir_y,  # new y
                x + dir_x,  # new x
                next_dir,  # next direction
                1 if direction != next_dir else moves_in_curr_dir + 1,  # moves in next direction
                path + [(y, x)]
            ))

    return None


def d17p2(lines: List[str]):
    # Removing all comments coming from previous part, will add comments only where code changed
    grid = parse_grid(lines)
    h, w = len(lines), len(lines[0])
    q = queue.PriorityQueue()
    # Change init: add first possible moves here, i.e. right 4 steps and down 4 steps
    q.put((sum(grid[0, i] for i in range(1, 4)), 0, 4, 0, 4, [(0, i) for i in range(4)]))
    q.put((sum(grid[i, 0] for i in range(1, 4)), 4, 0, 0, 4, [(i, 0) for i in range(4)]))
    visited = set()
    while q:
        curr_sum, y, x, direction, moves_in_curr_dir, path = q.get()

        if y == h - 1 and x == w - 1:
            return curr_sum + grid[y, x]

        if (y, x, direction, moves_in_curr_dir) in visited:
            continue
        visited.add((y, x, direction, moves_in_curr_dir))

        next_possible_dir = [(direction - 1) % 4, (direction + 1) % 4]
        # Change max moves in current direction
        if moves_in_curr_dir < 10:
            next_possible_dir.append(direction)

        for next_dir in next_possible_dir:
            dir_y, dir_x = MOVES[next_dir]
            # Change filling in the queue: if we change direction we account for at least 4 moves, hence we sum 3 cells
            # in next direction; otherwise we do the same stuff as before
            new_sum = curr_sum + grid[y, x]
            if direction == next_dir:
                if not (0 <= y + dir_y < h and 0 <= x + dir_x < w):
                    continue
                new_y, new_x = y + dir_y, x + dir_x
                new_path = path + [(y, x)]
            else:
                if not (0 <= y + 4 * dir_y < h and 0 <= x + 4 * dir_x < w):
                    continue
                new_sum += sum(grid[y + i * dir_y, x + i * dir_x] for i in range(1, 4))
                new_y, new_x = y + 4 * dir_y, x + 4 * dir_x
                new_path = path + [(y, x)] + [(y + i * dir_y, x + i * dir_x) for i in range(1, 4)]
            q.put((
                new_sum,
                new_y,
                new_x,
                next_dir,
                4 if direction != next_dir else moves_in_curr_dir + 1,
                new_path
            ))

    return None


if __name__ == '__main__':
    # Both solutions are slow today :(
    day, year = 17, 2023
    lines = python_utils.get_input_as_lines(day, year)
    print(f'Part 1: {d17p1(lines)}')
    print(f'Part 2: {d17p2(lines)}')
