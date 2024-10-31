from typing import List

import python_utils


def d1p1(lines: List[str]):
    return sum(python_utils.ravel_list(python_utils.parse_ints(line) for line in lines))


def d1p2(lines: List[str]):
    frequencies = {0}
    cumsum = 0
    while True:
        for freq in python_utils.ravel_list(python_utils.parse_ints(line) for line in lines):
            cumsum += freq
            if cumsum in frequencies:
                return cumsum
            frequencies.add(cumsum)


if __name__ == '__main__':
    day, year = 1, 2018
    lines = python_utils.get_input_as_lines(day, year)
    print(f'Part 1: {d1p1(lines)}')
    print(f'Part 2: {d1p2(lines)}')
