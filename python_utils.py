import re
from pathlib import Path


def get_input(day, year):
    with open(Path(__file__).parent / f"{year}" / "input_files" / f"input{day}.txt", 'r') as input_file:
        return input_file.read().strip()


def get_input_as_lines(day, year):
    return get_input(day, year).split('\n')


def parse_ints(text):
    return [int(x) for x in re.findall(r'-?\d+', text)]


def splitter(list_to_split, split_val):
    ret = []
    curr = []
    for val in list_to_split:
        if val == split_val:
            ret.append(curr)
            curr = []
            continue
        curr.append(val)

    if len(curr) > 0:
        if len(curr[-1]) < 1:
            curr.pop(-1)
        ret.append(curr)

    return ret
