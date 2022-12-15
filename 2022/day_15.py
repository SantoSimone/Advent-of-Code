import re
from typing import List

import python_utils


def brute_force(data, row):
    # This day had to come... BRUTE FORCE

    # Compute the range of x's occupied at given row
    xmin_xmax = []
    for sx, sy, bx, by in data:
        range_at_y = abs(sx - bx) + abs(sy - by) - abs(sy - row)
        if range_at_y >= 0:
            xmin_xmax.append((sx - range_at_y, sx + range_at_y))

    # Merge ranges of x: first we sort them, then for each range we extend the previous one if they overlap
    xmin_max = sorted(xmin_xmax)
    xranges = [list(xmin_max[0])]
    for xmin, xmax in xmin_max[1:]:
        if xranges[-1][1] >= xmin - 1:
            xranges[-1][1] = max(xranges[-1][1], xmax)
        else:
            xranges.append([xmin, xmax])

    return xranges


def d15p1(lines: List[str]):
    parsed_lines = [re.match('Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)', line)
                    for line in lines]

    parsed_lines = [tuple(map(int, line.groups())) for line in parsed_lines]

    return sum([xmax - xmin for xmin, xmax in brute_force(parsed_lines, 2_000_000)])


def d15p2(lines: List[str]):
    parsed_lines = [re.match('Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)', line)
                    for line in lines]

    parsed_lines = [tuple(map(int, line.groups())) for line in parsed_lines]

    # The only one working must have two ranges
    for row in range(4_000_000):
        xranges = brute_force(parsed_lines, row)
        if len(xranges) > 1:
            return (xranges[0][1] + 1) * 4_000_000 + row

    return -1


if __name__ == '__main__':
    lines = python_utils.get_input_as_lines(15, 2022)
    print(f"Part 1: {d15p1(lines)}")
    print(f"Part 2: {d15p2(lines)}")
