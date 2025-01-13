import collections
import functools
from typing import List

import python_utils


@functools.lru_cache
def mix(a: int, b: int):
    return a ^ b


@functools.lru_cache
def prune(a: int):
    return a % 16777216


@functools.lru_cache
def generate_number(num: int):
    num = prune(mix(num, num * 64))
    num = prune(mix(num, num // 32))
    num = prune(mix(num, num * 2048))
    return num


def d22p1(lines: List[str]):
    # Straight compute everything, a bit slow (~2 sec)

    tot = 0
    for line in lines:
        num = int(line)
        for _ in range(2000):
            num = generate_number(num)
        tot += num
    return tot


def d22p2(lines: List[str]):
    # Add a dictionary in which we add up the current price whenever we see the same sequence
    # Plus a dictionary that tells us if we already saw that sequence for the current buyer

    tot = collections.defaultdict(int)
    for line in lines:
        num = int(line)
        changes = []
        already_done = {}
        for _ in range(2000):
            new = generate_number(num)
            changes.append(new % 10 - num % 10)
            num = new
            if len(changes) > 4:
                changes.pop(0)
            if len(changes) == 4 and tuple(changes) not in already_done:
                tot[tuple(changes)] += num % 10
                already_done[tuple(changes)] = True

    return max(tot.values())


if __name__ == '__main__':
    day, year = 22, 2024
    lines = python_utils.get_input_as_lines(day, year)
    print(f'Part 1: {d22p1(lines)}')
    print(f'Part 2: {d22p2(lines)}')
