import re
from collections import defaultdict
from typing import List, Tuple

import numpy as np

from python_utils import get_input_as_lines, splitter, parse_ints, get_input


class Lanternfish:
    def __init__(self, init_timer: int = 8):
        self.timer = init_timer

    def tick(self) -> bool:
        """
        Ticks timer and returns whether to spawn another lanternfish or not
        """
        self.timer -= 1

        if self.timer == -1:
            self.timer = 6
            return True

        return False


def d6p1(input_text: str, num_days: int):
    # I decided to keep this solution even if it not scalable
    fishes = [Lanternfish(i) for i in parse_ints(input_text)]
    for day in range(num_days):
        add = 0
        for f in fishes:
            add += 1 if f.tick() else 0
        fishes.extend([Lanternfish() for _ in range(add)])

    return len(fishes)


def d6p2(input_text: str, num_days: int):
    # We need to optimize things now, i.e. use a dict
    fishes = defaultdict(int)
    for days_remaining in parse_ints(text):
        fishes[days_remaining] += 1

    for day in range(num_days):
        next_day = defaultdict(int)
        for k, v in fishes.items():
            if k == 0:
                next_day[6] += v
                next_day[8] += v
            else:
                next_day[k - 1] += v

        fishes = next_day.copy()

    return sum(fishes.values())


if __name__ == '__main__':
    text = get_input(6, 2021)
    print(f"Part 1: {d6p1(text, 80)}")
    print(f"Part 2: {d6p2(text, 256)}")
