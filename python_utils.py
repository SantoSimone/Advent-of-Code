import re
from pathlib import Path
from typing import List, Any


def get_input(day: int, year: int, raw: bool = False):
    with open(Path(__file__).parent / f"{year}" / "input_files" / f"input{day}.txt", 'r') as input_file:
        data = input_file.read()
        if not raw:
            data = data.strip()

        return data


def get_input_as_lines(day: int, year: int):
    return get_input(day, year).split('\n')


def parse_ints(text: str):
    return [int(x) for x in re.findall(r'-?\d+', text)]


def splitter(list_to_split: List[Any], split_val: Any):
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
