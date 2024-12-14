from typing import List

import cv2
import numpy as np

import python_utils


def d14p1(lines: List[str]):
    # Simple uniform linear motion, then some if else to get the buckets (maybe it can be written better)

    grid_h, grid_w = 103, 101
    half_h, half_w = grid_h // 2, grid_w // 2

    buckets = [0] * 4
    for line in lines:
        p_x, p_y, v_x, v_y = python_utils.parse_ints(line)
        final_x = (p_x + v_x * 100) % grid_w
        final_y = (p_y + v_y * 100) % grid_h

        if final_x == half_w or final_y == half_h:
            continue

        if final_x < half_w and final_y < half_h:
            idx = 0
        elif final_x > half_w and final_y < half_h:
            idx = 1
        elif final_x < half_w and final_y > half_h:
            idx = 2
        else:
            idx = 3
        buckets[idx] += 1

    return python_utils.multiply(buckets)


def d14p2(lines: List[str]):
    # Strange day, we go back to single step iteration instead of the other way around
    # I write all images then I check with my naked eyes :)
    # I would bet that looking at connected components we could find a rule instead of looking by hand

    grid_h, grid_w = 103, 101

    robots = [python_utils.parse_ints(line) for line in lines]
    for i in range(1, 100_000):
        robots = [
            ((x + v_x) % grid_w, (y + v_y) % grid_h, v_x, v_y)
            for x, y, v_x, v_y in robots
        ]

        grid = np.zeros(shape=(grid_h, grid_w))
        for x, y, _, _ in robots:
            grid[y, x] = 255

        cv2.imwrite(f'./imgs/img{i}.png', grid)


if __name__ == '__main__':
    day, year = 14, 2024
    lines = python_utils.get_input_as_lines(day, year)
    print(f'Part 1: {d14p1(lines)}')
    print(f'Part 2: {d14p2(lines)}')
