from typing import List, Dict

import python_utils


def parse_inputs(lines: List[str]) -> Dict[int, int]:
    layers = {}
    for line in lines:
        idx, scanner_range = python_utils.parse_ints(line)
        layers[idx] = scanner_range

    return layers


def d13p1(lines: List[str]):
    # Each scanner reaches the zero position every X steps, X depends on the range of the scanner

    layers = parse_inputs(lines)

    severity = 0
    for pos in range(max(layers) + 1):
        if pos in layers:
            scanner_range = layers[pos]
            mod = 2 * (scanner_range - 1)
            if pos % mod == 0:
                severity += pos * scanner_range

    return severity


def d13p2(lines: List[str]):
    # The elegant solution here is the chinese remainder theorem, but brute force required just a bunch of seconds :)
    layers = parse_inputs(lines)

    start = 0
    while True:
        for layer_idx in range(max(layers) + 1):
            pos = start + layer_idx
            if layer_idx in layers:
                scanner_range = layers[layer_idx]
                mod = 2 * (scanner_range - 1)
                if pos % mod == 0:
                    start += 1
                    break
        else:
            return start


if __name__ == '__main__':
    day, year = 13, 2017
    lines = python_utils.get_input_as_lines(day, year)
    print(f'Part 1: {d13p1(lines)}')
    print(f'Part 2: {d13p2(lines)}')
