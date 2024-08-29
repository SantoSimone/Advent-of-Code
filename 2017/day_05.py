from typing import List

import python_utils


def d5p1(lines: List[str]):
    instructions = list(map(int, lines))

    idx = steps = 0
    while 0 <= idx < len(instructions):
        curr_jump = instructions[idx]
        instructions[idx] += 1
        idx += curr_jump
        steps += 1

    return steps


def d5p2(lines: List[str]):
    instructions = list(map(int, lines))

    idx = steps = 0
    while 0 <= idx < len(instructions):
        curr_jump = instructions[idx]
        instructions[idx] = instructions[idx] + (1 if instructions[idx] < 3 else -1)
        idx += curr_jump
        steps += 1

    return steps


if __name__ == '__main__':
    day, year = 5, 2017
    lines = python_utils.get_input_as_lines(day, year)
    print(f'Part 1: {d5p1(lines)}')
    print(f'Part 2: {d5p2(lines)}')
