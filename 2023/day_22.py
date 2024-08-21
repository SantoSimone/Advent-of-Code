import collections
from typing import List

import python_utils


def solve_base_map(bricks: List):
    final_map = {}
    bricks_final_positions = []
    for i, brick in enumerate(bricks):
        start_pos, end_pos = brick
        all_voxels_2d = [(x, y)
                         for x in range(start_pos[0], end_pos[0] + 1)
                         for y in range(start_pos[1], end_pos[1] + 1)]

        all_voxels_xs = [x for x, y in all_voxels_2d]
        all_voxels_ys = [y for x, y in all_voxels_2d]
        all_zs = [z for x, y, z in final_map.keys() if x in all_voxels_xs and y in all_voxels_ys]
        lowest_z = max(all_zs) + 1 if all_zs else 1

        final_positions = []
        for x, y in all_voxels_2d:
            for range_z in range(end_pos[2] - start_pos[2] + 1):
                final_map[x, y, lowest_z + range_z] = i
                final_positions.append((x, y, lowest_z + range_z))

        bricks_final_positions.append(final_positions)

    supports = collections.defaultdict(set)
    supported = collections.defaultdict(set)
    for i, coords in enumerate(bricks_final_positions):
        # coords = [(x, y, z) for (x, y, z), v in final_map.items() if v == i]
        for x, y, z in coords:
            value_above = final_map.get((x, y, z + 1), 0)
            if value_above != 0 and value_above != i:
                supports[i].add(value_above)
                supported[value_above].add(i)

    return supports, supported


def d22p1(lines: List[str]):
    bricks = [
        tuple(tuple(map(int, coords.split(','))) for coords in line.split('~'))
        for line in lines
    ]
    bricks.sort(key=lambda k: min(k[0][2], k[1][2]))

    supports, supported = solve_base_map(bricks)
    destroyable = set(range(len(bricks)))
    for i, supp in supported.items():
        if len(supp) == 1:
            destroyable.discard(*supp)

    return len(destroyable)


def d22p2(lines: List[str]):
    bricks = [
        tuple(tuple(map(int, coords.split(','))) for coords in line.split('~'))
        for line in lines
    ]
    bricks.sort(key=lambda k: min(k[0][2], k[1][2]))

    supports, supported = solve_base_map(bricks)

    destroyed = 0
    for i, _ in enumerate(bricks):
        curr_destroyed = {i}
        q = supports[i]
        while q:
            curr = q.pop()
            if all(s in curr_destroyed for s in supported[curr]):
                curr_destroyed.add(curr)
                q = q.union(supports[curr])

        destroyed += len(curr_destroyed) - 1

    return destroyed


if __name__ == '__main__':
    day, year = 22, 2023
    lines = python_utils.get_input_as_lines(day, year)
    print(f'Part 1: {d22p1(lines)}')
    print(f'Part 2: {d22p2(lines)}')
