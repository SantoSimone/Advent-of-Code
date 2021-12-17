import itertools
import math
import re

import numpy as np

from python_utils import get_input


def simulate(vx: int, vy: int, x1: int, x2: int, y1: int, y2: int) -> int:
    pos = np.array([0, 0])
    max_height = -math.inf

    # Some shots are just too short, skip them
    if vx * (vx + 1) // 2 < x1:
        return max_height

    for _ in range(30000):
        pos += np.array([vx, vy])
        # another trick: we know that vx must be positive
        vx = max(vx - 1, 0)
        vy -= 1
        if pos[1] > max_height:
            max_height = pos[1]

        if x1 <= pos[0] <= x2 and y1 <= pos[1] <= y2:
            return max_height
        elif pos[0] > x2 and pos[1] < y2:
            # A trick to speed things up (depends on your input)
            return -math.inf

    return -math.inf


def d17p1(text: str):
    x1, x2, y1, y2 = map(int, re.findall(r'-?\d+', text))

    # Guess I can involve some physics here, but who cares -> brute force
    max_height = -math.inf
    for vx, vy in itertools.product(range(1, 100), range(1, 100)):
        h = simulate(vx, vy, x1, x2, y1, y2)
        if h > max_height:
            max_height = h

    return max_height


def d17p2(text: str):
    x1, x2, y1, y2 = map(int, re.findall(r'-?\d+', text))

    # We still like brute force, but we use adjust values on ranges to do less computation (depends on your input)
    count = 0
    for vx, vy in itertools.product(range(1, x2 + 1), range(y1, 150)):
        h = simulate(vx, vy, x1, x2, y1, y2)
        if h != -math.inf:
            count += 1

    return count


if __name__ == '__main__':
    text = get_input(17, 2021)
    text = text.replace('\n', '')
    print(f"Part 1: {d17p1(text)}")
    print(f"Part 2: {d17p2(text)}")
