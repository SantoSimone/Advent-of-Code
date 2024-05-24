import re
from collections import defaultdict
from typing import List

import python_utils


def d5p1(lines: List[str]):
    stacks = defaultdict(list)
    init_lines, commands = python_utils.splitter(lines, "")
    for line in reversed(init_lines[:-1]):
        for i, c in enumerate(line[1::4]):
            if c != " ":
                stacks[i + 1].append(c)
    for cmd in commands:
        num, src, dst = map(int, re.findall(r'\d+', cmd))
        to_move = [stacks[src].pop() for _ in range(num)]
        stacks[dst].extend(to_move)

    return [s[-1:] for s in stacks.values()]


def d5p2(lines: List[str]):
    stacks = defaultdict(list)
    init_lines, commands = python_utils.splitter(lines, "")
    for line in reversed(init_lines[:-1]):
        for i, c in enumerate(line[1::4]):
            if c != " ":
                stacks[i + 1].append(c)
    for cmd in commands:
        num, src, dst = map(int, re.findall(r'\d+', cmd))
        to_move = [stacks[src].pop() for _ in range(num)]
        stacks[dst].extend(reversed(to_move))

    return [s[-1:] for s in stacks.values()]


if __name__ == '__main__':
    lines = python_utils.get_input_as_lines(5, 2022)
    print(f"Part 1: {d5p1(lines)}")
    print(f"Part 2: {d5p2(lines)}")
