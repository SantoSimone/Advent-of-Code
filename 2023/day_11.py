import itertools
from typing import List

import python_utils


def parse_grid(lines: List[str], mul: int):
    galaxies = []
    filled_rows = set()
    filled_cols = set()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "#":
                galaxies.append((y, x))
                filled_rows.add(y)
                filled_cols.add(x)

    empty_rows = set(range(len(lines))).difference(filled_rows)
    empty_cols = set(range(len(lines[0]))).difference(filled_cols)

    expanded_galaxies = []
    for galaxy in galaxies:
        empty_rows_above = sum(y < galaxy[0] for y in empty_rows)
        empty_cols_before = sum(x < galaxy[1] for x in empty_cols)

        expanded_galaxies.append((galaxy[0] + empty_rows_above * mul, galaxy[1] + empty_cols_before * mul))

    return expanded_galaxies


def d11p1(lines: List[str]):
    galaxies = parse_grid(lines, 1)

    return sum(abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) for p1, p2 in itertools.combinations(galaxies, 2))


def d11p2(lines: List[str]):
    galaxies = parse_grid(lines, 999_999)

    return sum(abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) for p1, p2 in itertools.combinations(galaxies, 2))


if __name__ == '__main__':
    day, year = 11, 2023
    lines = python_utils.get_input_as_lines(day, year)
    print(f'Part 1: {d11p1(lines)}')
    print(f'Part 2: {d11p2(lines)}')
