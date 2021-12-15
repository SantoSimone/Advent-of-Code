import numpy as np

from python_utils import parse_ints, get_input


def d7p1(input_text: str):
    positions = parse_ints(input_text)
    optimal_pos = np.median(positions)
    fuel_needed = np.abs(positions - optimal_pos)

    return np.sum(fuel_needed)


def d7p2(input_text: str):
    # Not sure if this is the best solution, but it seems fair to me
    positions = parse_ints(input_text)
    min_fuel_needed = float('inf')

    for pos in range(min(positions), max(positions) + 1):
        fuel_needed = sum(
            map(
                lambda n: n * (n + 1) // 2,
                map(lambda p: abs(p - pos), positions)
            )
        )
        if fuel_needed < min_fuel_needed:
            min_fuel_needed = fuel_needed

    return min_fuel_needed


if __name__ == '__main__':
    text = get_input(7, 2021)
    # text = "16,1,2,0,4,2,7,1,2,14"
    print(f"Part 1: {d7p1(text)}")
    print(f"Part 2: {d7p2(text)}")
