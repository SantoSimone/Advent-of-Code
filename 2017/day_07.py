import collections
import re
from typing import List, Dict, Tuple

import python_utils


def parse_inputs(lines: List[str]) -> Tuple[Dict[str, List[str]], Dict[str, str], Dict[str, int]]:
    supporting = collections.defaultdict(list)
    supported = {}
    weights = {}
    for line in lines:
        programs = re.findall(r'[a-z]+', line)

        supporting[programs[0]].extend(programs[1:])
        for p in programs[1:]:
            supported[p] = programs[0]

        weight = re.findall('\d+', line)[0]
        weights[programs[0]] = int(weight)

    return supported, supporting, weights


def d7p1(lines: List[str]):
    # The root program must be the only one that is supporting others but is not supported by any other program
    supported, supporting, _ = parse_inputs(lines)
    return set(supporting).difference(supported).pop()


def compute_sum(supporting: Dict[str, List[str]], weights: Dict[str, int], curr_program: str):
    return weights[curr_program] + sum([compute_sum(supporting, weights, s) for s in supporting[curr_program]])


def d7p2(lines: List[str]):
    # We walk down the "wrong path" (saving the last difference between good and wrong sums) up to the point where
    # we find that all children sums are good; then the solution is the current program's weight minus the last
    # difference saved
    supported, supporting, weights = parse_inputs(lines)
    root = set(supporting).difference(supported).pop()

    curr = root
    last_diff = 0
    while True:
        children = supporting[curr]
        sums = [compute_sum(supporting, weights, c) for c in children]
        if len(set(sums)) == 1:
            return weights[curr] - last_diff
        else:
            common_sum, wrong_sum = [x[0] for x in collections.Counter(sums).most_common(2)]
            last_diff = wrong_sum - common_sum
            wrong_idx = next(i for i, s in enumerate(sums) if s == wrong_sum)
            curr = children[wrong_idx]


if __name__ == '__main__':
    day, year = 7, 2017
    lines = python_utils.get_input_as_lines(day, year)
    print(f'Part 1: {d7p1(lines)}')
    print(f'Part 2: {d7p2(lines)}')
