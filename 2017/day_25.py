import collections
from typing import List

import python_utils


def get_state_commands(lines: List[str]):
    commands = {}
    for state_idx in range(3, len(lines), 10):
        curr_state = lines[state_idx][-2]
        commands[curr_state] = {}
        for idx in range(state_idx + 1, state_idx + 9, 4):
            curr_val = bool(int(lines[idx][-2]))
            commands[curr_state][curr_val] = [bool(int(lines[idx + 1][-2])),
                                              1 if 'right' in lines[idx + 2] else -1,
                                              lines[idx + 3][-2]]

    return commands


def d25p1(lines: List[str]):
    state = lines[0][-2]
    rounds = python_utils.parse_ints(lines[1])[0]
    tape = collections.defaultdict(bool)
    commands = get_state_commands(lines)
    cursor = 0
    for _ in range(rounds):
        val, move, state = commands[state][tape[cursor]]
        tape[cursor] = val
        cursor += move

    return sum(tape.values())


if __name__ == '__main__':
    day, year = 25, 2017
    lines = python_utils.get_input_as_lines(day, year)
    print(f'Part 1: {d25p1(lines)}')
