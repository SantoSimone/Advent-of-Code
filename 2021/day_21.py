import functools
import itertools
import re
from typing import Tuple

from python_utils import get_input


def d21p1(text: str):
    p1, p2 = map(int, re.findall(r'\d', text)[1::2])
    t1, t2 = 0, 0

    dice = 0
    switch = True
    while not (t1 >= 1000 or t2 >= 1000):
        v = sum([d % 10 + 1 for d in range(dice, dice + 3)]) % 10
        if switch:
            p1 = (p1 + v) if p1 + v <= 10 else p1 + v - 10
            t1 += p1
        else:
            p2 = (p2 + v) if p2 + v <= 10 else p2 + v - 10
            t2 += p2

        switch = not switch
        dice += 3

    return dice * (t1 if t1 < 1000 else t2)


def d21p2(text: str):
    start_1, start_2 = map(int, re.findall(r'\d', text)[1::2])

    @functools.lru_cache(maxsize=None)
    def play_game(p1: int, p2: int, t1: int, t2: int, switch: bool) -> Tuple[int, int]:
        if t1 >= 21:
            return 1, 0
        elif t2 >= 21:
            return 0, 1
        else:
            w1, w2 = 0, 0
            for v in map(sum, itertools.product([1, 2, 3], [1, 2, 3], [1, 2, 3])):
                if switch:
                    new_p = (p1 + v) if p1 + v <= 10 else p1 + v - 10
                    new_t = t1 + new_p
                    wins = play_game(new_p, p2, new_t, t2, not switch)
                else:
                    new_p = (p2 + v) if p2 + v <= 10 else p2 + v - 10
                    new_t = t2 + new_p
                    wins = play_game(p1, new_p, t1, new_t, not switch)
                w1 += wins[0]
                w2 += wins[1]

        return w1, w2

    return max(play_game(start_1, start_2, 0, 0, True))


if __name__ == '__main__':
    text = get_input(21, 2021)
    print(f"Part 1: {d21p1(text)}")
    print(f"Part 2: {d21p2(text)}")
