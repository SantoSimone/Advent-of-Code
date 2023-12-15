import collections
import re
from typing import List, Tuple

import python_utils


def hash_string(txt: str) -> int:
    # Core function of part 1
    curr_value = 0
    for c in txt:
        ascii = ord(c)
        curr_value += ascii
        curr_value *= 17
        curr_value = curr_value % 256

    return curr_value


def d15p1(input_text: str):
    return sum(hash_string(step) for step in input_text.split(','))


def find_in_box(box_list: List[Tuple[str, str]], query_label: str) -> int:
    # Utility to check if label is already in box
    idx = -1
    for i, (box_label, val) in enumerate(box_list):
        if box_label == query_label:
            idx = i
            break
    return idx


def d15p2(input_text: str):
    # I don't deserve this wall of text for such a simple problem :(
    
    boxes = collections.defaultdict(list)
    for step in input_text.split(','):
        reg_result = re.findall(r"(\w+)(-|=)(\d*)", step)[0]
        label = reg_result[0]
        operation = reg_result[1]
        hash_value = hash_string(label)
        if operation == '=':
            idx = find_in_box(boxes[hash_value], label)
            if idx == -1:
                boxes[hash_value].append((label, reg_result[2]))
            else:
                boxes[hash_value][idx] = (label, reg_result[2])
        else:
            idx = find_in_box(boxes[hash_value], label)
            if idx > -1:
                boxes[hash_value].pop(idx)

    total = 0
    for box_num, slots in boxes.items():
        for slot_num, (_, focal_length) in enumerate(slots):
            total += (box_num + 1) * (slot_num + 1) * int(focal_length)
    return total


if __name__ == '__main__':
    day, year = 15, 2023
    txt = python_utils.get_input(day, year)
    print(f'Part 1: {d15p1(txt)}')
    print(f'Part 2: {d15p2(txt)}')
