from typing import List

import numpy as np

from python_utils import get_input_as_lines

'''Dirty code today, not in the mood to make it fancier'''


def d3p1(lines: List[str]):
    all_numbers = np.asarray([[int(char) for char in line] for line in lines])
    gamma_rate = ""
    epsilon_rate = ""
    for c in range(all_numbers.shape[1]):
        one_is_most_frequent = np.sum(all_numbers[:, c]) > (all_numbers.shape[0] / 2)
        gamma_rate += '1' if one_is_most_frequent else '0'
        epsilon_rate += '0' if one_is_most_frequent else '1'

    return int(epsilon_rate, 2) * int(gamma_rate, 2)
    # return np.sum(moves[:, 0]) * np.sum(moves[:, 1])


def d3p2(lines: List[str]):
    all_numbers = np.asarray([[int(char) for char in line] for line in lines])
    oxygen = 0
    co2 = 0
    oxygen_mask = [True] * all_numbers.shape[0]
    co2_mask = [True] * all_numbers.shape[0]

    for c in range(all_numbers.shape[1]):
        one_is_most_frequent = np.sum(all_numbers[oxygen_mask][:, c]) >= (all_numbers[oxygen_mask].shape[0] / 2)
        oxygen_mask = [r and all_numbers[i][c] == (1 if one_is_most_frequent else 0)
                       for i, r in enumerate(oxygen_mask)]

        one_is_most_frequent = np.sum(all_numbers[co2_mask][:, c]) >= (all_numbers[co2_mask].shape[0] / 2)
        co2_mask = [r and all_numbers[i][c] == (0 if one_is_most_frequent else 1)
                    for i, r in enumerate(co2_mask)]

        if len(all_numbers[oxygen_mask]) == 1:
            oxygen_str = ''.join([i for i in all_numbers[oxygen_mask][0].astype(str)])
            oxygen = int(oxygen_str, 2)

        if len(all_numbers[co2_mask]) == 1:
            co2_str = ''.join([i for i in all_numbers[co2_mask][0].astype(str)])
            co2 = int(co2_str, 2)

    return co2 * oxygen


if __name__ == '__main__':
    lines = get_input_as_lines(3, 2021)
    print(f"Part 1: {d3p1(lines)}")
    print(f"Part 2: {d3p2(lines)}")
