import re
from typing import List

import more_itertools

from python_utils import get_input_as_lines


def d3p1(lines: List[str]):
    rucksacks = [more_itertools.chunked(l, len(l) // 2) for l in lines]
    sharing = [set(p1).intersection(p2).pop() for p1, p2 in rucksacks]
    priorities = [ord(x) - ord('a') + 1 if x.islower() else ord(x) - ord('A') + 27 for x in sharing]

    return sum(priorities)


def d3p2(lines: List[str]):
    groups = more_itertools.chunked(lines, 3)
    sharing = [set(r1).intersection(r2).intersection(r3).pop() for r1, r2, r3 in groups]
    priorities = [ord(x) - ord('a') + 1 if x.islower() else ord(x) - ord('A') + 27 for x in sharing]

    return sum(priorities)


if __name__ == '__main__':
    lines = get_input_as_lines(3, 2022)
    print(f"Part 1: {d3p1(lines)}")
    print(f"Part 2: {d3p2(lines)}")
