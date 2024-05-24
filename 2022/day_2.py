import re
from typing import List

from python_utils import get_input_as_lines


def d2p1(lines: List[str]):
    values = {
        "A": 1, "B": 2, "C": 3,
        "X": 1, "Y": 2, "Z": 3
    }
    score = 0
    for line in lines:
        enemy, me = re.findall(r'\w', line)
        res = (values[me] - values[enemy]) % 3
        win = 2 if res == 1 else (1 if res == 0 else 0)
        score += values[me] + win * 3
    return score


def d2p2(lines: List[str]):
    values = {
        "A": 1, "B": 2, "C": 3,
        "X": -1, "Y": 0, "Z": 1
    }
    score = 0
    for line in lines:
        enemy, res = re.findall(r'\w', line)
        res = values[res]
        me = (values[enemy] + res - 1) % 3 + 1
        win = 2 if res == 1 else (1 if res == 0 else 0)
        score += me + win * 3
    return score


if __name__ == '__main__':
    lines = get_input_as_lines(2, 2022)
    print(f"Part 1: {d2p1(lines)}")
    print(f"Part 2: {d2p2(lines)}")
