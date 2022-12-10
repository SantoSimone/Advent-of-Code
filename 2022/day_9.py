from collections import defaultdict
from typing import List

import numpy as np

import python_utils


def d9p1(lines: List[str]):
    values = {
        "L": np.array([-1, 0]),
        "R": np.array([1, 0]),
        "U": np.array([0, 1]),
        "D": np.array([0, -1])
    }
    commands = []
    for line in lines:
        splits = line.split(' ')
        commands.append((values[splits[0]], int(splits[1])))

    head_pos = np.array([0, 0])
    tail_pos = np.array([0, 0])
    visited = defaultdict(int)
    visited[(0, 0)] += 1
    for dir, num in commands:
        while num > 0:
            head_pos += dir
            horizontal_diff = head_pos[0] - tail_pos[0]
            vertical_diff = head_pos[1] - tail_pos[1]

            if abs(horizontal_diff) + abs(vertical_diff) > 2:
                move = np.array([np.sign(horizontal_diff), np.sign(vertical_diff)])
            else:
                h_shift = max(-1, min(1, np.sign(horizontal_diff) * (abs(horizontal_diff) - 1)))
                v_shift = max(-1, min(1, np.sign(vertical_diff) * (abs(vertical_diff) - 1)))
                move = np.array([h_shift, v_shift])

            tail_pos += move
            visited[tuple(tail_pos)] += 1
            num -= 1

    return sum([1 for v in visited.values() if v > 0])


def d9p2(lines: List[str]):
    values = {
        "L": np.array([-1, 0]),
        "R": np.array([1, 0]),
        "U": np.array([0, 1]),
        "D": np.array([0, -1])
    }
    commands = []
    for line in lines:
        splits = line.split(' ')
        commands.append((values[splits[0]], int(splits[1])))

    positions = [np.array([0, 0]) for i in range(10)]
    visited = defaultdict(int)
    visited[(0, 0)] += 1
    for dir, num in commands:
        while num > 0:
            positions[0] += dir
            for i in range(1, 10):
                horizontal_diff = positions[i - 1][0] - positions[i][0]
                vertical_diff = positions[i - 1][1] - positions[i][1]

                if abs(horizontal_diff) + abs(vertical_diff) > 2:
                    move = np.array([np.sign(horizontal_diff), np.sign(vertical_diff)])
                else:
                    h_shift = max(-1, min(1, np.sign(horizontal_diff) * (abs(horizontal_diff) - 1)))
                    v_shift = max(-1, min(1, np.sign(vertical_diff) * (abs(vertical_diff) - 1)))
                    move = np.array([h_shift, v_shift])

                positions[i] += move
                if i == 9:
                    visited[tuple(positions[i])] += 1
            num -= 1

    return sum([1 for v in visited.values() if v > 0])


if __name__ == '__main__':
    lines = python_utils.get_input_as_lines(9, 2022)
    print(f"Part 1: {d9p1(lines)}")
    print(f"Part 2: {d9p2(lines)}")
