import itertools
from typing import List, Tuple

import python_utils

DIRS = {
    'v': (1, 0),
    '^': (-1, 0),
    '<': (0, -1),
    '>': (0, 1)
}


class Object:
    __class_id_iter: int = itertools.count()

    def __init__(self, y: int, x: int, width: int = 0):
        self.y = y
        self.x = x
        self.width = width
        self.id = next(Object.__class_id_iter)

    def __eq__(self, other):
        return (self.y, self.x) == other or (self.y, self.x + self.width) == other

    def __repr__(self):
        return f"Obj - y: {self.y} x: {self.x} - ID: {self.id}"

    def __hash__(self):
        return self.id

    def would_collide(self, dir: Tuple[int, int], other: "Object") -> bool:
        if self.id == other.id:
            return False
        dir_y, dir_x = dir
        return (
                (self.y + dir_y, self.x + dir_x) == (other.y, other.x) or
                (self.y + dir_y, self.x + self.width + dir_x) == (other.y, other.x) or
                (self.y + dir_y, self.x + dir_x) == (other.y, other.x + other.width)
        )


def d15p1(lines: List[str]):
    # Some recursive simulation. A bit slow, but it works.

    grid_lines, movements = python_utils.splitter(lines, '')
    grid = python_utils.parse_grid(grid_lines)

    robot = next(Object(y=i, x=j) for (i, j), v in grid.items() if v == '@')
    boxes = [Object(y=i, x=j) for (i, j), v in grid.items() if v == 'O']

    def try_move(obj, dir):
        nonlocal grid
        dir_y, dir_x = dir

        if grid[obj.y + dir_y, obj.x + dir_x] == '#':
            return False

        should_move = True
        objects_in_the_way = [other_obj for other_obj in boxes if other_obj == (obj.y + dir_y, obj.x + dir_x)]
        if len(objects_in_the_way) == 1:
            other_obj = objects_in_the_way[0]
            should_move = try_move(other_obj, dir)

        if should_move:
            obj.y += dir_y
            obj.x += dir_x

            return True

        return False

    for move in ''.join(movements):
        try_move(robot, DIRS[move])

    return sum(100 * obj.y + obj.x for obj in boxes)


def d15p2(lines: List[str]):
    # Had some problems with maximum recursion, hence I decided to move to an iterative approach
    # Parsing changes a bit and the new algorithm should solve both part 1 and part 2

    grid_lines, movements = python_utils.splitter(lines, '')
    grid = {}
    robot, boxes = None, []
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == '#':
                grid[i, j * 2] = '#'
                grid[i, j * 2 + 1] = '#'
            else:
                if c == 'O':
                    boxes.append(Object(y=i, x=j * 2, width=1))
                elif c == '@':
                    robot = Object(y=i, x=j * 2)

                grid[i, j * 2] = '.'
                grid[i, j * 2 + 1] = '.'

    for move_idx, move in enumerate(''.join(movements)):
        dir_y, dir_x = DIRS[move]
        objects_to_move = [robot]
        idx = 0
        while idx < len(objects_to_move):
            obj = objects_to_move[idx]
            idx += 1

            if grid[obj.y + dir_y, obj.x + dir_x] == '#' or grid[obj.y + dir_y, obj.x + obj.width + dir_x] == '#':
                objects_to_move = []
                break

            objects_in_the_way = [other_obj for other_obj in boxes if obj.would_collide(DIRS[move], other_obj)]
            if len(objects_in_the_way) > 0:
                objects_to_move.extend(objects_in_the_way)
                continue

        for obj in set(objects_to_move):
            obj.y += dir_y
            obj.x += dir_x

    return sum(100 * obj.y + obj.x for obj in boxes)


if __name__ == '__main__':
    day, year = 15, 2024
    lines = python_utils.get_input_as_lines(day, year)
    print(f'Part 1: {d15p1(lines)}')
    print(f'Part 2: {d15p2(lines)}')
