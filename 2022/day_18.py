import itertools
from collections import defaultdict
from typing import List

import python_utils


def neighbors(pos):
    x, y, z = pos
    for addx, addy, addz in [(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]:
        yield x + addx, y + addy, z + addz


def get_voxels(lines: List[str]):
    voxels = defaultdict(int)
    for line in lines:
        x, y, z = python_utils.parse_ints(line)
        voxels[(x, y, z)] = 1

    return voxels


def try_exit(start, xrange, yrange, zrange, voxels):
    inner = 0
    candidates = [start]
    visited = set()
    while candidates:
        curr = candidates.pop()
        if curr in visited:
            continue
        visited.add(curr)
        if curr[0] not in xrange or curr[1] not in yrange or curr[2] not in zrange:
            return 0, visited

        for pos in neighbors(curr):
            if pos in voxels:
                inner += 1
            elif pos not in visited:
                candidates.append(pos)

    return inner, visited


def d18p1(lines: List[str]):
    voxels = get_voxels(lines)

    # Start considering all sides are free, uncheck all those covered by neighbours
    original_keys = list(voxels.keys())
    sides = 6 * len(original_keys)
    for x, y, z in original_keys:
        for addx, addy, addz in [(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]:
            sides -= voxels[x + addx, y + addy, z + addz]

    return sides


def d18p2(lines: List[str]):
    voxels = get_voxels(lines)
    minX = min([x for x, y, z in voxels.keys()])
    maxX = max([x for x, y, z in voxels.keys()])
    minY = min([y for x, y, z in voxels.keys()])
    maxY = max([y for x, y, z in voxels.keys()])
    minZ = min([z for x, y, z in voxels.keys()])
    maxZ = max([z for x, y, z in voxels.keys()])

    xrange = range(minX, maxX + 1)
    yrange = range(minY, maxY + 1)
    zrange = range(minZ, maxZ + 1)

    exterior = d18p1(lines)
    all_visited = set()
    for pos in itertools.product(xrange, yrange, zrange):
        if pos not in voxels and pos not in all_visited:
            inner, visited = try_exit(pos, xrange, yrange, zrange, voxels)
            exterior -= inner
            all_visited |= visited

    return exterior


if __name__ == '__main__':
    lines = python_utils.get_input_as_lines(18, 2022)
    #     lines = """2,2,2
    # 1,2,2
    # 3,2,2
    # 2,1,2
    # 2,3,2
    # 2,2,1
    # 2,2,3
    # 2,2,4
    # 2,2,6
    # 1,2,5
    # 3,2,5
    # 2,1,5
    # 2,3,5""".splitlines()
    print(f"Part 1: {d18p1(lines)}")
    print(f"Part 2: {d18p2(lines)}")
