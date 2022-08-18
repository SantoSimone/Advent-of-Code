import collections
import itertools
from typing import List
from python_utils import get_input_as_lines


def d20p1(lines: List[str]):
    algo = [1 if char == '#' else 0 for char in lines[0]]

    pixels = {}
    for y, line in enumerate(lines[2:]):
        for x, char in enumerate(line):
            pixels[y, x] = 1 if char == '#' else 0

    def process_position(y: int, x: int, it: int) -> int:
        neighbors = [(y + i, x + j) for i, j in itertools.product([-1, 0, 1], [-1, 0, 1])]
        binary = ''.join(
            str(pixels[p]) if p in pixels.keys() else str(default)
            for p in neighbors
        )
        return algo[int(binary, 2)]

    default = 0
    for it in range(2):
        min_y, max_y = min([y for y, x in pixels.keys()]), max([y for y, x in pixels.keys()])
        min_x, max_x = min([x for y, x in pixels.keys()]), max([x for y, x in pixels.keys()])
        pixels = {
            (y, x): process_position(y, x, it)
            for y, x in itertools.product(range(min_y - 1, max_y + 2), range(min_x - 1, max_x + 2))
        }

        default = algo[-1] if it % 2 and algo[0] else algo[0]

    return sum(pixels.values())


def d20p2(lines: List[str]):
    # It is not THAT slow, will come back for an optimization one day
    algo = [1 if char == '#' else 0 for char in lines[0]]

    pixels = {}
    for y, line in enumerate(lines[2:]):
        for x, char in enumerate(line):
            pixels[y, x] = 1 if char == '#' else 0

    def process_position(y: int, x: int, it: int) -> int:
        neighbors = [(y + i, x + j) for i, j in itertools.product([-1, 0, 1], [-1, 0, 1])]
        binary = ''.join(
            str(pixels[p]) if p in pixels.keys() else str(default)
            for p in neighbors
        )
        return algo[int(binary, 2)]

    default = 0
    for it in range(50):
        min_y, max_y = min([y for y, x in pixels.keys()]), max([y for y, x in pixels.keys()])
        min_x, max_x = min([x for y, x in pixels.keys()]), max([x for y, x in pixels.keys()])
        pixels = {
            (y, x): process_position(y, x, it)
            for y, x in itertools.product(range(min_y - 1, max_y + 2), range(min_x - 1, max_x + 2))
        }

        default = algo[-1] if it % 2 and algo[0] else algo[0]

    return sum(pixels.values())


if __name__ == '__main__':
    lines = get_input_as_lines(20, 2021)
    print(f"Part 1: {d20p1(lines)}")
    print(f"Part 2: {d20p2(lines)}")
