import collections
from typing import List

import python_utils


def d1p1(lines: List[str]):
    # Pythonic way of messing with this problem, everything is lazy evaluated
    # To break thing up:
    # i) parse the ints inside a line of text -> tuple of two integers
    # ii) zip all the tuples, i.e. take the first number of each tuple and create a list, then do the same with the
    # second one of each tuple
    # iii) sort the two lists
    left, right = map(sorted, zip(*map(python_utils.parse_ints, lines)))
    return sum(abs(l - r) for l, r in zip(left, right))


def d1p2(lines: List[str]):
    # No need to sort now. Use a Counter to easily get the counts of each number
    left, right = zip(*map(python_utils.parse_ints, lines))
    right_counter = collections.Counter(right)

    return sum(l * right_counter.get(l, 0) for l in left)


if __name__ == '__main__':
    day, year = 1, 2024
    lines = python_utils.get_input_as_lines(day, year)
    print(f'Part 1: {d1p1(lines)}')
    print(f'Part 2: {d1p2(lines)}')
