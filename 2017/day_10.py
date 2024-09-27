import functools
import operator
from typing import List

import more_itertools

import python_utils


def d10p1(input_text: str):
    numbers = list(range(256))
    curr_idx = 0
    skip = 0
    for length in python_utils.parse_ints(input_text):
        run(numbers, curr_idx, length)
        curr_idx = (curr_idx + length + skip) % 256
        skip += 1

    return numbers[0] * numbers[1]


def run(numbers: List[int], curr_idx: int, length: int):
    # i) Find the indices that will be swapped in this round
    # ii) Build the list of numbers that will be swapped and reverse it
    # iii) Simply swap following the indices
    # NOTE: List is modified "in-place" due to python lists behaviour, hence we do not need any return

    indices_to_swap = [(curr_idx + i) % 256 for i in range(length)]
    numbers_to_swap = list(reversed([numbers[idx] for idx in indices_to_swap]))
    for idx, swap in zip(indices_to_swap, numbers_to_swap):
        numbers[idx] = swap


def d10p2(input_text: str):
    lengths = [ord(c) for c in input_text] + [17, 31, 73, 47, 23]
    numbers = list(range(256))
    curr_idx = 0
    skip = 0
    for _ in range(64):
        for length in lengths:
            run(numbers, curr_idx, length)
            curr_idx = (curr_idx + length + skip) % 256
            skip += 1

    hash = []
    for chunk in more_itertools.chunked(numbers, 16):
        res = functools.reduce(operator.xor, chunk)
        to_str = hex(res)[2:]
        if len(to_str) == 1:
            to_str = '0' + to_str
        hash.append(to_str)

    return ''.join(hash)


if __name__ == '__main__':
    day, year = 10, 2017
    txt = python_utils.get_input(day, year)
    print(f'Part 1: {d10p1(txt)}')
    print(f'Part 2: {d10p2(txt)}')
