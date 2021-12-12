import itertools
import re
from collections import defaultdict
from typing import List, Tuple, Dict, Optional

import numpy as np

from python_utils import get_input_as_lines, splitter, parse_ints, get_input


def parse_paths(lines: List[str]) -> Dict[str, List[str]]:
    paths = defaultdict(list)
    for line in lines:
        s, e = line.split('-')
        paths[s].append(e)
        paths[e].append(s)

    return paths


def d12p1(lines: List[str]):
    paths = parse_paths(lines)
    pos = 'start'

    def rec(pos: str, visited: List[str]) -> Optional[List[List[str]]]:
        if pos == 'end':
            # We return a double list as each position should return the List of possible paths starting from itself
            return [[pos]]

        possible_paths = []
        for p in paths[pos]:
            if p in visited and p.islower():
                continue

            possible = rec(p, visited + [pos])
            if possible is not None:
                possible_paths.extend([[pos] + route for route in possible])

        return possible_paths if len(possible_paths) > 0 else None

    return len(rec(pos, []))


def d12p2(lines: List[str]):
    # The additional check requires a little bit of waiting
    paths = parse_paths(lines)
    pos = 'start'

    def rec(pos: str, visited: List[str]) -> Optional[List[List[str]]]:
        if pos == 'end':
            # We return a double list as each position should return the List of possible paths starting from itself
            return [[pos]]

        possible_paths = []
        next_visited = visited + [pos]
        already_visited_twice = any([next_visited.count(pp) > 1 and pp.islower() for pp in paths.keys()])
        for p in paths[pos]:
            if p == 'start' or (p != 'end' and
                                p.islower() and
                                next_visited.count(p) > 0 and
                                already_visited_twice):
                continue

            possible = rec(p, next_visited)
            if possible is not None:
                possible_paths.extend([[pos] + route for route in possible])

        return possible_paths if len(possible_paths) > 0 else None

    return len(rec(pos, []))


if __name__ == '__main__':
    lines = get_input_as_lines(12, 2021)
    print(f"Part 1: {d12p1(lines)}")
    print(f"Part 2: {d12p2(lines)}")
