from typing import List

import numpy as np

import python_utils


def get_wins(race_time: int, race_distance: int):
    wins = 0
    for t_i in range(1, race_time):
        d_i = t_i * (race_time - t_i)
        if d_i > race_distance:
            wins += 1
    return wins


def d6p1(lines: List[str]):
    times = python_utils.parse_ints(lines[0])
    distances = python_utils.parse_ints(lines[1])
    wins = [get_wins(race_time, race_distance) for race_time, race_distance in zip(times, distances)]
    return np.prod(wins)


def d6p2(lines: List[str]):
    # Few seconds of waiting time, I'm okay with it
    # EDIT: but I wanted to find a proper solution :)
    race_time = python_utils.parse_ints(lines[0].replace(' ', ''))[0]
    race_distance = python_utils.parse_ints(lines[1].replace(' ', ''))[0]
    min_time = int((race_time - np.sqrt(race_time ** 2 - 4 * race_distance)) / 2)
    max_time = int((race_time + np.sqrt(race_time ** 2 - 4 * race_distance)) / 2)
    return max_time - min_time


if __name__ == '__main__':
    day, year = 6, 2023
    lines = python_utils.get_input_as_lines(day, year)
    print(f'Part 1: {d6p1(lines)}')
    print(f'Part 2: {d6p2(lines)}')
