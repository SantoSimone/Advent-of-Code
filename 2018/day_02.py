import collections
from typing import List

import python_utils


def d2p1(lines: List[str]):
    twos = threes = 0
    for line in lines:
        counter = collections.Counter(line)
        if any(v == 2 for v in counter.values()):
            twos += 1
        if any(v == 3 for v in counter.values()):
            threes += 1
    return twos * threes


def d2p2(lines: List[str]):
    for i, line1 in enumerate(lines):
        for line2 in lines[i + 1:]:
            if sum(c1 == c2 for c1, c2 in zip(line1, line2)) == len(line1) - 1:
                return ''.join(c1 for c1, c2 in zip(line1, line2) if c1 == c2)

    return None


if __name__ == '__main__':
    day, year = 2, 2018
    lines = python_utils.get_input_as_lines(day, year)
    print(f'Part 1: {d2p1(lines)}')
    print(f'Part 2: {d2p2(lines)}')
