from typing import List

import python_utils


def find_history(starting_values: List[int]) -> List[List[int]]:
    history = [starting_values]
    while any(x != 0 for x in starting_values):
        starting_values = [starting_values[i + 1] - x for i, x in enumerate(starting_values[:-1])]
        history.append(starting_values)

    return history


def d9p1(lines: List[str]):
    next_values = []

    for line in lines:
        history = find_history(python_utils.parse_ints(line))

        next_val = history[-1][-1]
        for seq in reversed(history[:-1]):
            next_val += seq[-1]

        next_values.append(next_val)

    return sum(next_values)


def d9p2(lines: List[str]):
    prev_values = []

    for line in lines:
        history = find_history(python_utils.parse_ints(line))

        prev_val = history[-1][0]
        for seq in reversed(history[:-1]):
            prev_val = seq[0] - prev_val

        prev_values.append(prev_val)

    return sum(prev_values)


if __name__ == '__main__':
    day, year = 9, 2023
    lines = python_utils.get_input_as_lines(day, year)
    print(f'Part 1: {d9p1(lines)}')
    print(f'Part 2: {d9p2(lines)}')
