import collections
import copy
import itertools
import re
from collections import defaultdict
from typing import List, Tuple, Dict, Optional

import numpy as np

from python_utils import get_input_as_lines, splitter, parse_ints, get_input
import more_itertools


def parse_inputs(lines: List[str]):
    polymer, rules = splitter(lines, '')

    rules = {
        pair: ch for pair, ch in [re.findall('\w+', line) for line in rules]
        # ''.join([p0, p1]): ''.join([p0, ch, p1]) for p0, p1, ch in [re.findall('\w', line) for line in rules]
    }

    return polymer[0], rules


def d14p1(lines: List[str]):
    polymer, rules = parse_inputs(lines)

    for _ in range(10):
        pairs = map(lambda x: ''.join(x), more_itertools.windowed(polymer, 2, 1))
        insertions = [rules[p] if p in rules.keys() else '' for p in pairs]
        insertions += ['']  # (not so beautiful) trick to make lists same length
        polymer = ''.join([x for t in zip(*[list(polymer), insertions]) for x in t])

    counts = collections.Counter(polymer)

    return counts.most_common()[0][1] - counts.most_common()[-1][1]


def d14p2(lines: List[str]):
    # We need to switch to a dict to count frequencies
    polymer, rules = parse_inputs(lines)

    pairs = more_itertools.windowed(polymer, 2, 1)
    frequencies = defaultdict(int)
    for p in pairs:
        frequencies[''.join(p)] += 1

    for _ in range(40):
        next_frequencies = defaultdict(int)
        for k, v in frequencies.items():
            # next_frequencies[k] -= v
            next_frequencies[k[0] + rules[k]] += v
            next_frequencies[rules[k] + k[1]] += v
        frequencies = copy.deepcopy(next_frequencies)

    counts = defaultdict(int)
    for k, v in frequencies.items():
        counts[k[0]] += v / 2
        counts[k[1]] += v / 2

    sorted_counts = sorted(counts.values())
    return int(sorted_counts[-1] - sorted_counts[0])


if __name__ == '__main__':
    lines = get_input_as_lines(14, 2021)
    print(f"Part 1: {d14p1(lines)}")
    print(f"Part 2: {d14p2(lines)}")
