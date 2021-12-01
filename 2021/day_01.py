import numpy as np

from python_utils import parse_ints, get_input


def d1p1(day: int):
    values = parse_ints(get_input(day=day, year=2021))
    increases = np.sum(
        [values[i - 1] < values[i] for i in range(1, len(values))]
    )
    print(f"Number of increases is {increases}")


def d1p2(day: int):
    values = parse_ints(get_input(day=day, year=2021))
    increases = np.sum(
        [np.sum(values[i - 3:i]) < np.sum(values[i - 2:i + 1])
         for i in range(3, len(values))]
    )
    print(f"Number of increases is {increases}")


if __name__ == '__main__':
    day = 1
    d1p1(day)
    d1p2(day)
