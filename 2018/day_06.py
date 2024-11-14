import collections
from typing import List

import python_utils


def dist(p1: List[int], p2: List[int]):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def d6p1(lines: List[str]):
    vertices = [python_utils.parse_ints(l) for l in lines]
    min_x = min(v[0] for v in vertices)
    max_x = max(v[0] for v in vertices)
    min_y = min(v[1] for v in vertices)
    max_y = max(v[1] for v in vertices)

    infinite_vertices = [i for i, v in enumerate(vertices)
                         if v[0] in (min_x, max_x) or v[1] in (min_y, max_y)]
    areas = collections.defaultdict(int)
    for x in range(min_x, max_x):
        for y in range(min_y, max_y):
            distances = [dist([x, y], v) for v in vertices]
            distances_with_indices = sorted(enumerate(distances), key=lambda x: x[1])
            if distances_with_indices[0][1] == distances_with_indices[1][1]:
                continue

            areas[distances_with_indices[0][0]] += 1

    for i in infinite_vertices:
        if i in areas.keys():
            areas.pop(i)

    return max(areas.values())


def d6p2(lines: List[str]):
    vertices = [python_utils.parse_ints(l) for l in lines]
    min_x = min(v[0] for v in vertices)
    max_x = max(v[0] for v in vertices)
    min_y = min(v[1] for v in vertices)
    max_y = max(v[1] for v in vertices)

    region = 0
    for x in range(min_x, max_x):
        for y in range(min_y, max_y):
            distances = [dist([x, y], v) for v in vertices]
            total_dist = sum(distances)
            if total_dist < 10_000:
                region += 1

    return region


if __name__ == '__main__':
    day, year = 6, 2018
    lines = python_utils.get_input_as_lines(day, year)
    print(f'Part 1: {d6p1(lines)}')
    print(f'Part 2: {d6p2(lines)}')
