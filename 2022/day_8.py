import re
from typing import List

import numpy as np

import python_utils


def d8p1(lines: List[str]):
    trees = np.zeros((len(lines), len(lines[0])), dtype=np.uint8)
    for i, line in enumerate(lines):
        trees[i] = np.array(list(re.findall('\d', line)))

    count = 0
    for ((r, c), h) in np.ndenumerate(trees):
        if (
                np.all(trees[:r, c] < h) or  # up
                np.all(trees[r + 1:, c] < h) or  # down
                np.all(trees[r, :c] < h) or  # left
                np.all(trees[r, c + 1:] < h)  # right
        ):
            count += 1

    return count


def d8p2(lines: List[str]):
    trees = np.zeros((len(lines), len(lines[0])), dtype=np.uint8)
    for i, line in enumerate(lines):
        trees[i] = np.array(list(re.findall('\d', line)))

    max_score = 0
    for ((r, c), h) in np.ndenumerate(trees):
        scores = []
        for (i, j) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            score = 0
            mul = 1
            while 0 <= r + i * mul < trees.shape[0] and 0 <= c + j * mul < trees.shape[1]:
                score += 1
                if trees[r + i * mul, c + j * mul] >= h:
                    break
                mul += 1
            scores.append(score)

        if np.prod(scores) > max_score:
            max_score = np.prod(scores)

    return max_score


if __name__ == '__main__':
    lines = python_utils.get_input_as_lines(8, 2022)
    print(f"Part 1: {d8p1(lines)}")
    print(f"Part 2: {d8p2(lines)}")
