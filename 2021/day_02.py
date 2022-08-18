from typing import List

import numpy as np

from python_utils import get_input_as_lines


def parse_commands(lines: List[str]):
    moves = []
    for line in lines:
        move_str, x = line.split(' ')
        x = int(x)
        if move_str == 'forward':
            moves.append((x, 0))
        else:
            moves.append((0, x) if move_str == 'down' else (0, -x))

    return np.asarray(moves)


def d2p1(lines: List[str]):
    moves = parse_commands(lines)
    return np.sum(moves[:, 0]) * np.sum(moves[:, 1])


def d2p2(lines: List[str]):
    moves = parse_commands(lines)
    aim = 0
    horizontal = 0
    depth = 0
    for move in moves:
        aim += move[1]
        horizontal += move[0]
        depth += aim * move[0]

    return horizontal * depth


if __name__ == '__main__':
    day = 2
    lines = get_input_as_lines(day, 2021)
    print(f"Part 1: {d2p1(lines)}")
    print(f"Part 2: {d2p2(lines)}")
