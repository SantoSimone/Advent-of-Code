import datetime
import os
import re
from pathlib import Path
from typing import Union, Iterable, List, Tuple, Dict

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


def parse_grid(lines: List[str]) -> Dict[Tuple[int, int], str]:
    """Helper function to parse a grid from a list of lines - (y, x) format"""
    return {
        (i, j): c
        for i, line in enumerate(lines)
        for j, c in enumerate(line)
    }


def multiply(arr: Iterable):
    res = 1
    for v in arr:
        res *= v
    return res


def cumsum(arr: Iterable):
    tot = 0
    for v in arr:
        tot += v
        yield tot


# down, left, up, right
DIRS = ((1, 0), (0, -1), (-1, 0), (0, 1))


def grid_neighbors(pos: Tuple[int, int], directions: Iterable[Tuple[int, int]] = DIRS) -> Iterable[Tuple[int, int]]:
    """ Helper function for classic grid problems where neighbors should be computed.
     Default behaviour computes the 4 neighbors with no diagonal directions.

    :param pos: position from which neighbors will be computed - (y, x) format
    :param directions: all possible directions where neighbor could be
    :return: an iterable of all the possible neighbors
    """

    y, x = pos
    for dir_y, dir_x in directions:
        yield y + dir_y, x + dir_x


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


def ravel_list(l: List):
    """
    Ravel any nested list into a flat list

    :param l: any list with any level of nesting
    :return: a flat list of items
    """
    for item in l:
        if isinstance(item, list):
            yield from ravel_list(item)
        else:
            yield item


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
