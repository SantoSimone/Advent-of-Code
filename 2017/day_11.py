import numpy as np

import python_utils

DIR = {
    # q, r, s
    'n': np.array([0, -1, 1]),
    'ne': np.array([1, -1, 0]),
    'nw': np.array([-1, 0, 1]),
    's': np.array([0, 1, -1]),
    'se': np.array([1, 0, -1]),
    'sw': np.array([-1, 1, 0])
}


def d11p1(input_text: str):
    # Many thanks to https://www.redblobgames.com/grids/hexagons/ for the in-depth explanation of how to deal with
    # hexagonal grids

    pos = np.array([0, 0, 0])
    for d in input_text.split(','):
        pos += DIR[d]

    return int(np.abs(pos).sum() / 2)


def d11p2(input_text: str):
    pos = np.array([0, 0, 0])
    max_dist = 0
    for d in input_text.split(','):
        pos += DIR[d]
        dist = int(np.abs(pos).sum() / 2)
        if dist > max_dist:
            max_dist = dist

    return max_dist


if __name__ == '__main__':
    day, year = 11, 2017
    txt = python_utils.get_input(day, year)
    print(f'Part 1: {d11p1(txt)}')
    print(f'Part 2: {d11p2(txt)}')
