import collections
from typing import List

import python_utils


def d3p1(lines: List[str]):
    grid = collections.defaultdict(int)
    for line in lines:
        claim_id, x, y, w, h = python_utils.parse_ints(line)
        for i in range(w):
            for j in range(h):
                grid[x + i, y + j] += 1

    return len([k for k, v in grid.items() if v > 1])


def overlapping(line1: str, line2: str) -> bool:
    _, x1, y1, w1, h1 = python_utils.parse_ints(line1)
    _, x2, y2, w2, h2 = python_utils.parse_ints(line2)

    return x1 + w1 >= x2 and x2 + w2 >= x1 and y1 + h1 >= y2 and y2 + w2 >= y1


def d3p2(lines: List[str]):
    overlaps = set()
    lines = list(map(python_utils.parse_ints, lines))
    ids = set([claim_id for claim_id, *_ in lines])
    grid = {}
    for claim_id, x, y, w, h in lines:
        for i in range(w):
            for j in range(h):
                if (x + i, y + j) in grid:
                    overlaps = overlaps.union({claim_id, grid[x + i, y + j]})
                grid[x + i, y + j] = claim_id

    return ids.difference(overlaps).pop()


if __name__ == '__main__':
    day, year = 3, 2018
    lines = python_utils.get_input_as_lines(day, year)
    print(f'Part 1: {d3p1(lines)}')
    print(f'Part 2: {d3p2(lines)}')
