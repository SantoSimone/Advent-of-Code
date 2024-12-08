import itertools
from typing import List

import python_utils


def d8p1(lines: List[str]):
    nodes = {
        (i, j): c
        for i, line in enumerate(lines)
        for j, c in enumerate(line)
    }

    frequencies = set(nodes.values())
    frequencies.remove('.')
    antinodes = set()
    for frequency in frequencies:
        all_nodes = [(i, j) for (i, j), f in nodes.items() if f == frequency]
        for (i1, j1), (i2, j2) in itertools.combinations(all_nodes, 2):
            # (i_dir, j_dir) is the vector node2 -> node1
            i_dir = i1 - i2
            j_dir = j1 - j2
            if (i1 + i_dir, j1 + j_dir) in nodes:
                antinodes.add((i1 + i_dir, j1 + j_dir))
            if (i2 - i_dir, j2 - j_dir) in nodes:
                antinodes.add((i2 - i_dir, j2 - j_dir))

    return len(antinodes)


def d8p2(lines: List[str]):
    # Simply add a while loop when computing antinodes

    nodes = {
        (i, j): c
        for i, line in enumerate(lines)
        for j, c in enumerate(line)
    }

    frequencies = set(nodes.values())
    frequencies.remove('.')
    antinodes = set()
    for frequency in frequencies:
        all_nodes = [(i, j) for (i, j), f in nodes.items() if f == frequency]
        for (i1, j1), (i2, j2) in itertools.combinations(all_nodes, 2):
            antinodes.add((i1, j1))
            antinodes.add((i2, j2))

            # (i_dir, j_dir) is the vector node2 -> node1
            i_dir = i1 - i2
            j_dir = j1 - j2
            while (i1 + i_dir, j1 + j_dir) in nodes:
                antinodes.add((i1 + i_dir, j1 + j_dir))
                i1 += i_dir
                j1 += j_dir

            while (i2 - i_dir, j2 - j_dir) in nodes:
                antinodes.add((i2 - i_dir, j2 - j_dir))
                i2 -= i_dir
                j2 -= j_dir

    return len(antinodes)


if __name__ == '__main__':
    day, year = 8, 2024
    lines = python_utils.get_input_as_lines(day, year)
    print(f'Part 1: {d8p1(lines)}')
    print(f'Part 2: {d8p2(lines)}')
