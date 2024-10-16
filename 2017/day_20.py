import collections
from typing import List

import numpy as np

import python_utils


def d20p1(lines: List[str]):
    # First we try brute-forcing <3
    particles = np.array([python_utils.parse_ints(line) for line in lines])

    closest_for = 0
    closest = 0
    while True:
        if closest_for > 10_000:
            break
        particles[:, 3:6] += particles[:, 6:]
        particles[:, :3] += particles[:, 3:6]

        distances = np.abs(particles[:, :3]).sum(1)
        new_closest = np.argmin(distances)
        closest_for = closest_for + 1 if closest == new_closest else 0
        closest = new_closest

    return closest


def d20p2(lines: List[str]):
    particles = np.array([python_utils.parse_ints(line) for line in lines])
    remaining = 0
    not_collided_for = 0
    while True:
        if not_collided_for > 1_000:
            break
        particles[:, 3:6] += particles[:, 6:]
        particles[:, :3] += particles[:, 3:6]

        positions = particles[:, :3]
        pos_counter = collections.Counter([tuple(p) for p in positions.tolist()])
        for p, v in pos_counter.items():
            if v == 1:
                continue

            indices = np.argwhere(np.all(particles[:, :3] == p, 1))
            particles = np.delete(particles, indices, 0)

        new_remaining = len(particles)
        not_collided_for = not_collided_for + 1 if new_remaining == remaining else 0
        remaining = new_remaining

    return remaining


if __name__ == '__main__':
    day, year = 20, 2017
    lines = python_utils.get_input_as_lines(day, year)
    print(f'Part 1: {d20p1(lines)}')
    print(f'Part 2: {d20p2(lines)}')
