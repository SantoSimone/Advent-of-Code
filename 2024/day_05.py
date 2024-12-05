import collections
from typing import List

import python_utils


def d5p1(lines: List[str]):
    ordering, to_produce = python_utils.splitter(lines, '')
    condition = collections.defaultdict(list)
    for line in ordering:
        x, y = python_utils.parse_ints(line)
        condition[y].append(x)

    middle = 0
    for line in to_produce:
        nums = python_utils.parse_ints(line)
        for i, num in enumerate(nums):
            if any((cond in nums and cond not in nums[:i]) for cond in condition[num]):
                break
        else:
            middle += nums[len(nums) // 2]

    return middle


def d5p2(lines: List[str]):
    ordering, to_produce = python_utils.splitter(lines, '')
    condition = collections.defaultdict(list)
    for line in ordering:
        x, y = python_utils.parse_ints(line)
        condition[y].append(x)

    wrong = []
    for line in to_produce:
        nums = python_utils.parse_ints(line)
        for i, num in enumerate(nums):
            if any((cond in nums and cond not in nums[:i]) for cond in condition[num]):
                wrong.append(nums)
                break

    middle = 0
    for nums in wrong:
        corrected = []
        while len(corrected) != len(nums):
            all_cond = [set(condition[num]).intersection(nums).difference(corrected) for num in nums]
            next_add = next(num for num, cond in zip(nums, all_cond) if len(cond) == 0 and num not in corrected)
            corrected.append(next_add)

        middle += corrected[len(corrected) // 2]

    return middle


if __name__ == '__main__':
    day, year = 5, 2024
    lines = python_utils.get_input_as_lines(day, year)
    print(f'Part 1: {d5p1(lines)}')
    print(f'Part 2: {d5p2(lines)}')
