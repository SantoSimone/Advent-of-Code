import functools
import re
from typing import List, Tuple

import python_utils


def create_all_possibilities(line: str):
    candidates = [line]
    permutations = []
    while candidates:
        curr = candidates.pop()
        if "?" in curr:
            candidates.append(curr.replace('?', '.', 1))
            candidates.append(curr.replace('?', '#', 1))
        else:
            permutations.append(curr)

    return permutations


def count_groups(line: str):
    return list(map(len, re.findall(r'#+', line)))


def d12p1(lines: List[str]):
    tot = 0
    for line in lines:
        expected_groups = python_utils.parse_ints(line)
        for candidate in create_all_possibilities(line):
            if count_groups(candidate) == expected_groups:
                tot += 1

    return tot


@functools.cache
def compute_solutions(substring: str, counts: Tuple[int], curr_tag_count=0):
    # Recursive function (with caching power) that branches at each "?" and handles the behaviour for each case
    if not substring:
        return not counts and not curr_tag_count

    total_solutions = 0
    possible = [".", "#"] if substring[0] == "?" else substring[0]
    for c in possible:
        if c == "#":
            total_solutions += compute_solutions(substring[1:], counts, curr_tag_count + 1)
        else:
            if curr_tag_count:
                if counts and counts[0] == curr_tag_count:
                    total_solutions += compute_solutions(substring[1:], counts[1:])
            else:
                total_solutions += compute_solutions(substring[1:], counts)
    return total_solutions


def d12p2(lines: List[str]):
    strings_and_counts = []
    for line in lines:
        substring, counts = line.split(' ')
        counts = tuple(python_utils.parse_ints(counts))
        strings_and_counts.append((substring, counts))

    sol_counts = [compute_solutions("?".join([substring] * 5) + ".", counts * 5)
                  for substring, counts in strings_and_counts]

    return sum(sol_counts)


if __name__ == '__main__':
    day, year = 12, 2023
    lines = python_utils.get_input_as_lines(day, year)
    print(f'Part 1: {d12p1(lines)}')
    print(f'Part 2: {d12p2(lines)}')
