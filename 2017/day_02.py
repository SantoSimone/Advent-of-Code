import itertools
from typing import List

import python_utils


def d2p1(lines: List[str]):
    spreadsheet = [python_utils.parse_ints(line) for line in lines]

    checksum = 0
    for line in spreadsheet:
        min_val, max_val = min(line), max(line)
        checksum += max_val - min_val

    return checksum


def d2p2(lines: List[str]):
    spreadsheet = [python_utils.parse_ints(line) for line in lines]

    checksum = 0
    for line in spreadsheet:
        for n1, n2 in itertools.combinations(line, r=2):
            n1, n2 = max(n1, n2), min(n1, n2)

            if (n1 % n2) == 0:
                checksum += n1 // n2

    return checksum


if __name__ == '__main__':
    day, year = 2, 2017
    lines = python_utils.get_input_as_lines(day, year)
    print(f'Part 1: {d2p1(lines)}')
    print(f'Part 2: {d2p2(lines)}')
