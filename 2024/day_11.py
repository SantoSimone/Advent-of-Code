import collections
import functools
import itertools
import math
from typing import List

import python_utils


@functools.lru_cache()
def blink(stone: int) -> List[int]:
    if stone == 0:
        return [1]

    num_digits = int(math.log10(stone) + 1)
    if num_digits % 2 == 0:
        return divmod(stone, 10 ** (num_digits // 2))
    else:
        return [stone * 2024]


def d11p1(input_text: str):
    # We start with simple brute force, but we take the free caching from python standard lib

    stones = python_utils.parse_ints(input_text)
    for _ in range(25):
        stones = list(itertools.chain(*[
            blink(stone)
            for stone in stones
        ]))

    return len(stones)


def d11p2(input_text: str):
    # Obviously brute force wouldn't work. We exploit the fact that order is not needed here, so we can simply keep
    # track of how many stone numbers we have and compute the next step only once per round

    stones = python_utils.parse_ints(input_text)
    stones = collections.Counter(stones)
    for _ in range(75):
        new_stones = collections.Counter()
        for stone, count in stones.items():
            blink_stones = blink(stone)
            for s in blink_stones:
                new_stones[s] += count
        stones = new_stones

    return sum(stones.values())


if __name__ == '__main__':
    day, year = 11, 2024
    txt = python_utils.get_input(day, year)
    print(f'Part 1: {d11p1(txt)}')
    print(f'Part 2: {d11p2(txt)}')
