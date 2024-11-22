import collections
from typing import List, Tuple

import python_utils


def run_generation(pots: str, start_idx: int) -> Tuple[str, int]:
    pots = collections.defaultdict(lambda: '.', {i: c for i, c in enumerate(pots)})
    new_pots = {}
    for idx in range(min(pots.keys()) - 2, max(pots.keys()) + 3):
        batch = pots[idx - 2] + pots[idx - 1] + pots[idx] + pots[idx + 1] + pots[idx + 2]
        if batch in rules:
            new_pots[idx] = rules[batch]
        else:
            new_pots[idx] = '.'

    pots = ''.join(new_pots.values())
    pots = pots.rstrip('.')
    first_idx = pots.index('#')
    if first_idx > 4:
        pots = pots[first_idx:]
        start_idx += first_idx
    start_idx -= 2

    return pots, start_idx


def d12p1(lines: List[str]):
    pots = lines[0].split(': ')[1]
    start_idx = 0

    global rules
    rules = {}
    for line in lines[2:]:
        p1, p2 = line.split(' => ')
        rules[p1] = p2

    for i in range(20):
        pots, start_idx = run_generation(pots, start_idx)

    return sum(i for i, c in zip(range(start_idx, start_idx + len(pots)), pots) if c == '#')


def d12p2(lines: List[str]):
    # `lru_cache` wasn't enough, but we hit cache. Then we can compute the loop size and manually find the final state

    pots = lines[0].split(': ')[1]

    global rules
    rules = {}
    for line in lines[2:]:
        p1, p2 = line.split(' => ')
        rules[p1] = p2

    start_idx = steps = 0
    cache = {}
    while True:
        pots, start_idx = run_generation(pots, start_idx)
        steps += 1

        if pots in cache:
            break
        cache[pots] = (steps, start_idx)

    # We found the loop: compute the remaining steps and how much the string has expanded, then find the solution
    divisor_steps = steps - cache[pots][0]
    expanding_start_idx = start_idx - cache[pots][1]
    repeated_steps = (50_000_000_000 - steps) // divisor_steps
    remaining_steps = (50_000_000_000 - steps) % divisor_steps
    start_idx += expanding_start_idx * repeated_steps
    for _ in range(remaining_steps):
        pots = run_generation(pots, start_idx)

    return sum(i for i, c in zip(range(start_idx, start_idx + len(pots)), pots) if c == '#')


if __name__ == '__main__':
    day, year = 12, 2018
    lines = python_utils.get_input_as_lines(day, year)
    print(f'Part 1: {d12p1(lines)}')
    print(f'Part 2: {d12p2(lines)}')
