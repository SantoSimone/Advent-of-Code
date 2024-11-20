import itertools

import numpy as np

import python_utils


def compute_power(x: int, y: int, serial: int):
    rack_id = x + 10
    return (((rack_id * y) + serial) * rack_id) // 100 % 10 - 5


def find_largest(powers: np.ndarray, window_size: int):
    # We reimplement (a sort of) convolution just for fun
    # Since we use top-left and only squares that are fully contained in the grid, we can avoid computing all positions

    max_sum, max_pos = powers[0, 0], (0, 0)
    for y in range(300 - window_size):
        for x in range(300 - window_size):
            curr_sum = powers[y:y + window_size, x:x + window_size].sum()
            if curr_sum > max_sum:
                max_sum = curr_sum
                max_pos = (x, y)

    return max_sum, max_pos


def d11p1(input_text: str):
    serial = int(input_text)

    power_levels = [compute_power(x, y, serial) for y, x in itertools.product(range(300), range(300))]

    grid = np.array(power_levels, dtype=np.int32).reshape(300, 300)

    # We reimplement convolution just for fun
    max_sum, max_pos = find_largest(grid, 3)

    return max_pos


def d11p2(input_text: str):
    # Simply brute force the search by tweaking the `find_largest`.. ~30 s computation, I will accept it
    serial = int(input_text)

    power_levels = [compute_power(x, y, serial) for y, x in itertools.product(range(300), range(300))]

    grid = np.array(power_levels, dtype=np.int32).reshape(300, 300)
    max_sum, max_pos = grid[0, 0], (0, 0, 1)
    for size in range(300):
        curr_max, curr_pos = find_largest(grid, size)
        if curr_max > max_sum:
            max_sum = curr_max
            max_pos = (*curr_pos, size)

    return max_pos


if __name__ == '__main__':
    day, year = 11, 2018
    txt = python_utils.get_input(day, year)
    print(f'Part 1: {d11p1(txt)}')
    print(f'Part 2: {d11p2(txt)}')
