import itertools
from typing import List, Iterable

import python_utils


def sub_levels(levels: List[int]) -> Iterable[List[int]]:
    # Create all the possible sub-lists of levels
    for i in range(len(levels)):
        yield levels[:i] + levels[i + 1:]


def check_strict(levels: List[int]) -> bool:
    lt, gt, diff, length = (
        # i) create a tuple where we store the 3 checks for each consecutive pair
        # ii) sum the results from all the checks (the result will be a tuple of 3 item with the sum of how many
        # pairs respected each check)
        # iii) create a tuple with the 3 checks plus the amount of levels in this chunk
        *map(sum, zip(*[(a < b, a > b, abs(a - b) <= 3)
                        for a, b in itertools.pairwise(levels)])),
        len(levels)
    )

    # If we have N levels, we N - 1 pairs
    return (lt == length - 1 or gt == length - 1) and diff == length - 1


def d2p1(lines: List[str]):
    # This lazy-evaluation thing is getting out of hands

    all_levels = map(python_utils.parse_ints, lines)
    return sum(map(check_strict, all_levels))


def d2p2(lines: List[str]):
    # Could optimize it a bit more but let's go with straight solution
    # First we check the full line, otherwise we check all the possible sub-lists
    # An optimization would be to check only the two sub-lists without the items from the first wrong pair

    all_levels = map(python_utils.parse_ints, lines)
    return sum(check_strict(levels) or any(map(check_strict, sub_levels(levels))) for levels in all_levels)


if __name__ == '__main__':
    day, year = 2, 2024
    lines = python_utils.get_input_as_lines(day, year)
    print(f'Part 1: {d2p1(lines)}')
    print(f'Part 2: {d2p2(lines)}')
