import operator
from typing import List, Callable

import python_utils


def evaluate_line(test_val: int, nums: List[int], operators: List[Callable]) -> int:
    # Iterate over the queue.

    q = [(nums[0], 1)]
    while q:
        tot, next_idx = q.pop()

        # If we are already over test_val, there's no need to go ahead
        if tot > test_val:
            continue

        # We reached the end of the nums, check if we are good
        if next_idx > len(nums) - 1:
            if test_val == tot:
                return test_val
            continue

        # Add new tot and next idx to the queue (for each possible operator)
        q.extend([
            (op(tot, nums[next_idx]), next_idx + 1)
            for op in operators
        ])

    return 0


def d7p1(lines: List[str]):
    # Simply follow the instructions and fill a list with current total and next idx

    operators = [operator.add, operator.mul]
    good = 0
    for line in lines:
        test_val, *nums = python_utils.parse_ints(line)
        good += evaluate_line(test_val, nums, operators)

    return good


def d7p2(lines: List[str]):
    # Add a lambda that joins numbers (we use some python tricks)
    # We add a lot of new combinations but it does end in a decent amount of time (~2 sec)

    new_op = lambda a, b: int(''.join(map(str, [a, b])))
    operators = [operator.add, operator.mul, new_op]
    good = 0
    for line in lines:
        test_val, *nums = python_utils.parse_ints(line)
        good += evaluate_line(test_val, nums, operators)

    return good


if __name__ == '__main__':
    day, year = 7, 2024
    lines = python_utils.get_input_as_lines(day, year)
    print(f'Part 1: {d7p1(lines)}')
    print(f'Part 2: {d7p2(lines)}')
