import collections
from typing import Dict, List

import python_utils


def score_group(groups: Dict[int, List[int]], idx: int, offset: int):
    return offset + sum([score_group(groups, c, offset + 1) for c in groups[idx]])


def d9p1(input_text: str):
    # First we construct the tree of groups, where each node is identified by its starting idx
    # Then we compute the score by offsetting the base value of each child

    idx = 0
    garbage = False
    start_group = []
    groups = collections.defaultdict(list)
    while idx < len(input_text):
        if input_text[idx] == '<':
            garbage = True
        elif input_text[idx] == '>':
            garbage = False
        elif garbage:
            if input_text[idx] == '!':
                idx += 1
        elif not garbage:
            if input_text[idx] == '{':
                start_group.append(idx)
            elif input_text[idx] == '}':
                curr_group_start = start_group.pop()
                if len(start_group) > 0:
                    groups[start_group[-1]].append(curr_group_start)

        idx += 1

    return score_group(groups, 0, 1)


def d9p2(input_text: str):
    idx = 0
    garbage = False
    non_canceled = 0
    while idx < len(input_text):
        if input_text[idx] == '<' and not garbage:
            garbage = True
        elif input_text[idx] == '>':
            garbage = False
        elif garbage:
            if input_text[idx] == '!':
                idx += 1
            else:
                non_canceled += 1

        idx += 1

    return non_canceled


if __name__ == '__main__':
    day, year = 9, 2017
    txt = python_utils.get_input(day, year)
    print(f'Part 1: {d9p1(txt)}')
    print(f'Part 2: {d9p2(txt)}')
