import datetime
import os
import re
from pathlib import Path
from typing import Union, Iterable

import requests


def setup_day(day: Union[int, str], year: Union[int, str]) -> None:
    """Downloads input file and puts it in proper position"""
    # Get cookies from the browser
    import browser_cookie3
    cj = browser_cookie3.chrome()

    # Download data
    res = requests.get(f"https://adventofcode.com/{year}/day/{day}/input", cookies=cj)

    # Put in proper position for loading
    os.makedirs(Path(__file__).parent / f"{year}" / "input_files", exist_ok=True)
    with open(f"{year}/input_files/input{day}.txt", "w") as f:
        f.write(res.text)


def get_input(day, year):
    with open(Path(__file__).parent / f"{year}" / "input_files" / f"input{day}.txt", 'r') as input_file:
        return input_file.read().strip()


def get_input_as_lines(day, year):
    return get_input(day, year).split('\n')


def parse_ints(text: str):
    return [int(x) for x in re.findall(r'-?\d+', text)]


def multiply(a: Iterable):
    res = 1
    for v in a:
        res *= v
    return res


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


def full_setup():
    today = datetime.datetime.today()
    day = input("Day to setup (default today)\t")
    year = input("Year to setup (default this year)\t")
    input_type = input("Is input as lines? y/n (default yes)\t")

    if day == '':
        day = str(today.day)
    if year == '':
        year = str(today.year)
    if input_type.lower() in ['', 'y']:
        input_param = "lines"
        param_str = "lines: List[str]"
        input_str = "lines = python_utils.get_input_as_lines(day, year)"
    else:
        input_param = "txt"
        param_str = "input_text: str"
        input_str = "txt = python_utils.get_input(day, year)"

    os.makedirs(f'{year}/input_files', exist_ok=True)
    with open(Path(__file__).parent / f"{year}" / f"day_{day.zfill(2)}.py", 'w') as f:
        f.write(
            f"""from typing import List
            
import python_utils


def d{day}p1({param_str}):
    return None


def d{day}p2({param_str}):
    return None


if __name__ == '__main__':
    day, year = {day}, {year}
    {input_str}
    print(f'Part 1: {{d{day}p1({input_param})}}')
    print(f'Part 2: {{d{day}p2({input_param})}}')
""")

    setup_day(day, year)


if __name__ == '__main__':
    full_setup()
