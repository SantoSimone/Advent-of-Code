import re
from typing import List, Tuple

import python_utils

MOVES = {'R': (0, 1), 'D': (1, 0), 'L': (0, -1), 'U': (-1, 0),
         '0': (0, 1), '1': (1, 0), '2': (0, -1), '3': (-1, 0), }


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


def d18p1(lines: List[str]):
    pos = (0, 0)
    coords = [pos]
    for line in lines[:-1]:
        y, x = coords[-1]
        move, amount, _ = re.match(r'(R|D|L|U) (\d+) \((.+)\)', line).groups()
        dir_y, dir_x = MOVES[move]
        coords.append((y + int(amount) * dir_y, x + int(amount) * dir_x))

    # Eventually, I learned how to measure the area of a given polygon, i.e. shoelace formula + pick's theorem
    area, perimeter = area_and_perimeter(coords)
    return area + perimeter // 2 + 1


def d18p2(lines: List[str]):
    pos = (0, 0)
    coords = [pos]
    for line in lines[:-1]:
        y, x = coords[-1]
        _, _, real_data = re.match(r'(R|D|L|U) (\d+) \(#(.+)\)', line).groups()
        move = real_data[-1]
        amount = int(real_data[:-1], 16)
        dir_y, dir_x = MOVES[move]
        coords.append((y + amount * dir_y, x + amount * dir_x))

    # Eventually, I learned how to measure the area of a given polygon, i.e. shoelace formula + pick's theorem
    area, perimeter = area_and_perimeter(coords)
    return area + perimeter // 2 + 1


if __name__ == '__main__':
    day, year = 18, 2023
    lines = python_utils.get_input_as_lines(day, year)
    print(f'Part 1: {d18p1(lines)}')
    print(f'Part 2: {d18p2(lines)}')
