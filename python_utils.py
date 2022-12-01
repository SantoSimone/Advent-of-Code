import numpy as np
import urllib.request
import re
import collections
import itertools
import heapq
import functools
import copy


def get_input(day, year):
    return urllib.request.urlopen(f'https://raw.githubusercontent.com/SantoSimone'
                                  f'/Advent-of-Code/2022/{year}/input_files/input'
                                  f'{day}.txt').read().decode('utf-8')


def get_input_as_lines(day, year):
    return get_input(day, year).split('\n')[:-1]


def parse_ints(text):
    return [int(x) for x in re.findall(r'\d+', text)]


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
