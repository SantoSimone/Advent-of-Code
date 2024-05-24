import re
from typing import List

import python_utils


def isin(start1: int, end1: int, start2: int, end2: int) -> bool:
    """Check if start1 - end1 is contained in start2 - end2"""
    return start1 >= start2 and end1 <= end2


def overlap(range1: set, range2: set) -> bool:
    return len(range1.intersection(range2)) > 0


def d4p1(lines: List[str]):
    # This solution should be faster than using set intersection (did not time it)
    assignments = [map(int, re.findall(r'\d+', l)) for l in lines]
    overlaps = [isin(s1, e1, s2, e2) or isin(s2, e2, s1, e1) for s1, e1, s2, e2 in assignments]
    return sum(overlaps)


def d4p2(lines: List[str]):
    # Set intersection is enough, guess this is optimizable using some if statements
    assignments = [map(int, re.findall(r'\d+', l)) for l in lines]
    as_ranges = [(set(range(s1, e1 + 1)), set(range(s2, e2 + 1))) for s1, e1, s2, e2 in assignments]
    overlaps = [overlap(r1, r2) for r1, r2 in as_ranges]
    return sum(overlaps)


if __name__ == '__main__':
    lines = python_utils.get_input_as_lines(4, 2022)
    print(f"Part 1: {d4p1(lines)}")
    print(f"Part 2: {d4p2(lines)}")
