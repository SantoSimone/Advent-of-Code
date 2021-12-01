import numpy as np

from python_utils import parse_ints, get_input


def d1p1(day: int):
    values = parse_ints(get_input(day=day, year=2021))
    increases = np.sum(np.diff(values) > 0)
    print(f"Number of increases is {increases}")


def d1p2(day: int):
    values = np.array(parse_ints(get_input(day=day, year=2021)))
    increases = np.sum((values[:-3] - values[3:]) < 0)
    print(f"Number of increases is {increases}")


if __name__ == '__main__':
    day = 1
    d1p1(day)
    d1p2(day)
