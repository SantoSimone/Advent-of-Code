from pathlib import Path
from typing import List, Tuple, Dict

# Standard directions: right, down, left, up (dir + 1 means turning right, dir - 1 means turning left)
DIRS = {
    '<': (0, -1),
    '>': (0, 1),
    '^': (-1, 0),
    'v': (1, 0),
}

SWITCH = {
    '\\<': '^',
    '/<': 'v',
    '\\>': 'v',
    '/>': '^',
    '\\^': '<',
    '/^': '>',
    '\\v': '>',
    '/v': '<',

    '0>': '^',
    '0<': 'v',
    '0^': '<',
    '0v': '>',

    '1>': '>',
    '1<': '<',
    '1^': '^',
    '1v': 'v',

    '2>': 'v',
    '2<': '^',
    '2^': '>',
    '2v': '<',
}


class Cart:
    def __init__(self, y: int, x: int, dir: str, cart_id: int):
        self.position = y, x
        self.dir = dir
        self.state = 0
        self.crashed = False
        self.cart_id = cart_id

    def move(self, grid_val: str):
        if grid_val in ['\\', '/']:
            self.dir = SWITCH[grid_val + self.dir]
        elif grid_val == '+':
            self.dir = SWITCH[f"{self.state}{self.dir}"]

            self.state = (self.state + 1) % 3

        add_y, add_x = DIRS[self.dir]
        y, x = self.position
        self.position = (y + add_y, x + add_x)

    def __repr__(self):
        return (f"y: {self.position[0]} - x: {self.position[1]} - dir: {self.dir} - state: {self.state} - "
                f"ID: {self.cart_id} - {self.crashed}")


def parse_inputs(lines: List[str]) -> Tuple[Dict[Tuple[int, int], str], List[Cart]]:
    grid = {}
    carts = []
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c in ['^', 'v']:
                carts.append(Cart(y, x, c, len(carts)))
                c = '|'
            elif c in ['<', '>']:
                carts.append(Cart(y, x, c, len(carts)))
                c = '-'

            grid[y, x] = c

    return grid, sorted(carts, key=lambda c: c.position)


def tick(carts: List[Cart], grid: Dict[Tuple[int, int], str]) -> List[Cart]:
    for c in carts:
        if c.crashed:
            continue
        c.move(grid[c.position])

        for c2 in carts:
            if c2.crashed or c.cart_id == c2.cart_id:
                continue

            if c.position == c2.position:
                c.crashed = True
                c2.crashed = True

    carts.sort(key=lambda c: c.position)
    return carts


def d13p1(lines: List[str]):
    # Enjoy object oriented programming, as it helps in correct crash handling
    # All movements are hard-coded as it was faster to implement
    grid, carts = parse_inputs(lines)

    while True:
        carts = tick(carts, grid)
        if any(c.crashed for c in carts):
            break

    return next(c for c in carts if c.crashed).position[::-1]


def d13p2(lines: List[str]):
    grid, carts = parse_inputs(lines)

    while True:
        if sum(not c.crashed for c in carts) == 1:
            break
        carts = tick(carts, grid)

    return next(c for c in carts if not c.crashed).position[::-1]


if __name__ == '__main__':
    day, year = 13, 2018
    with open(Path(__file__).parent / "input_files" / f"input{day}.txt", 'r') as input_file:
        lines = input_file.read().split('\n')
    print(f'Part 1: {d13p1(lines)}')
    print(f'Part 2: {d13p2(lines)}')
