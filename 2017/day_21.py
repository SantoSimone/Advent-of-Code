from typing import List, Tuple

import numpy as np

import python_utils


def parse_rules(lines: List[str]) -> List[Tuple[np.ndarray, np.ndarray]]:
    def parse_side(side: str):
        side_arr = None
        for chunk in side.strip().split('/'):
            new_line = np.array([1 if c == '#' else 0 for c in chunk])
            side_arr = np.vstack([side_arr, new_line]) if side_arr is not None else new_line

        return side_arr

    rules = []
    for line in lines:
        lhs, rhs = line.split('=>')
        lhs_arr = parse_side(lhs)
        rhs_arr = parse_side(rhs)

        # There are 8 possible flip/rot of a 2d matrix
        flipped = np.fliplr(lhs_arr)
        transformations = [
            lhs_arr,
            np.rot90(lhs_arr, 1),
            np.rot90(lhs_arr, 2),
            np.rot90(lhs_arr, 3),
            flipped,
            np.rot90(flipped, 1),
            np.rot90(flipped, 2),
            np.rot90(flipped, 3)
        ]

        rules.extend([(t, rhs_arr) for t in transformations])

    return rules


def get_match(tile, rules):
    for query, res in rules:
        if len(tile) == len(query) and np.all(tile == query):
            return res

    return tile


def round(pattern, rules):
    divisor = 2 if len(pattern) % 2 == 0 else 3

    new_arr = None
    for i in range(0, pattern.shape[0], divisor):
        new_line = None
        for j in range(0, pattern.shape[1], divisor):
            curr_tile = pattern[i:i + divisor, j:j + divisor]
            match = get_match(curr_tile, rules)
            new_line = np.hstack([new_line, match]) if new_line is not None else match

        new_arr = np.vstack([new_arr, new_line]) if new_arr is not None else new_line

    return new_arr


def d21p1(lines: List[str]):
    rules = parse_rules(lines)

    pattern = np.array([
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1],
    ])
    for _ in range(5):
        pattern = round(pattern, rules)

    return pattern.sum()


def d21p2(lines: List[str]):
    # Brute force won't work :(
    # But we can easily note that after 3 iteration a single 3x3 becomes 9 blocks (still 3x3)
    # Hence we only need to keep track of how many 3x3 we currently have and a little cache of how a 3x3 becomes after 3
    # iterations
    # In terms of storage we could use a map/dict for `new_blocks` instead of a list, but the latter was faster to
    # implement, so I went for it

    rules = parse_rules(lines)

    pattern = np.array([
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1],
    ])
    blocks = [pattern]
    transforms = {}
    for _ in range(6):  # Now we need only 18 / 3 iterations since we process 3 rounds at every iteration
        new_blocks = []
        for block in blocks:
            if block.tobytes() in transforms:
                new_blocks.extend(transforms[block.tobytes()])
            else:
                proc = block.copy()
                for i in range(3):
                    proc = round(proc, rules)
                transforms[block.tobytes()] = [
                    proc[i:i + 3, j:j + 3]
                    for i in range(0, proc.shape[0], 3)
                    for j in range(0, proc.shape[1], 3)
                ]
                new_blocks.extend(transforms[block.tobytes()])

        blocks = new_blocks

    return np.array(blocks).sum()


if __name__ == '__main__':
    day, year = 21, 2017
    lines = python_utils.get_input_as_lines(day, year)
    print(f'Part 1: {d21p1(lines)}')
    print(f'Part 2: {d21p2(lines)}')
