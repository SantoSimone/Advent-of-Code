import functools
import re
from typing import List

import python_utils


@functools.lru_cache
def find_towels(design: str):
    if design == '':
        return 1
    return sum([find_towels(design[len(t):]) for t in towels if design.startswith(t)])


def d19p1(lines: List[str]):
    # Implemented the brute force, worked on examples, couldn't finish on real input
    # Added lru_cache -> matter of ~0.5 sec

    global towels
    towels = re.findall(r'\w+', lines[0])

    return sum(find_towels(design) > 0 for design in lines[2:])


def d19p2(lines: List[str]):
    # That's a difference of 2 characters of code from part 1 :D
    global towels
    towels = re.findall(r'\w+', lines[0])

    return sum(find_towels(design) for design in lines[2:])


if __name__ == '__main__':
    day, year = 19, 2024
    lines = python_utils.get_input_as_lines(day, year)
    print(f'Part 1: {d19p1(lines)}')
    print(f'Part 2: {d19p2(lines)}')
