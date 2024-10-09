import functools
import time
from typing import Iterator

import python_utils


def d15p1(input_text: str):
    # Let's start with brute-force

    a, b = python_utils.parse_ints(input_text)
    factor_a, factor_b = 16807, 48271
    divisor = 2147483647

    total = 0
    for _ in range(40_000_000):
        a = (a * factor_a) % divisor
        b = (b * factor_b) % divisor
        bin_a = bin(a)[2:].zfill(16)
        bin_b = bin(b)[2:].zfill(16)
        if bin_a[-16:] == bin_b[-16:]:
            total += 1

    return total


@functools.lru_cache(maxsize=5_000_000_000)
def next_val(val: int, factor: int) -> int:
    return (val * factor) % 2147483647


def generator(base_val: int, factor: int, mod: int) -> Iterator[int]:
    while True:
        base_val = next_val(base_val, factor)
        # base_val = (base_val * factor) % 2147483647
        if base_val % mod == 0:
            yield bin(base_val)[2:].zfill(16)


def d15p2(input_text: str):
    # I thought that adding some caching would help, but it seems not.. we still brute-force :)

    a, b = python_utils.parse_ints(input_text)
    a = generator(a, 16807, 4)
    b = generator(b, 48271, 8)

    start = time.perf_counter()
    total = 0
    for _ in range(5_000_000):
        if next(a)[-16:] == next(b)[-16:]:
            total += 1
    print(f"{time.perf_counter() - start:.4f}")
    return total


if __name__ == '__main__':
    day, year = 15, 2017
    txt = python_utils.get_input(day, year)
    print(f'Part 1: {d15p1(txt)}')
    print(f'Part 2: {d15p2(txt)}')
