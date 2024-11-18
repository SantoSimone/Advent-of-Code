import collections
from typing import List

import more_itertools

import python_utils


def fill_marbles(marbles: List[int], next_val: int, curr_idx: int):
    fill_range = list(range(next_val, next_val + len(marbles[curr_idx:])))
    divisible = [i for i, x in enumerate(fill_range) if x % 23 == 0]
    if divisible:
        fill_range = fill_range[:divisible[0]]

    interleaved = list(more_itertools.interleave_longest(marbles[curr_idx:], fill_range))

    return marbles[:curr_idx] + interleaved, len(fill_range)


def d9p1(input_text: str):
    # Brute force the solution
    num_players, highest_marble = python_utils.parse_ints(input_text)
    scores = collections.defaultdict(int)
    marbles = [0, 1]
    curr_idx = 1
    curr_player = 0
    for marble in range(2, highest_marble + 1):
        if marble % 23 == 0:
            curr_idx = (curr_idx - 7) % len(marbles)
            rm_marble = marbles.pop(curr_idx)
            if curr_idx > len(marbles):
                curr_idx = 0
            scores[curr_player] += marble + rm_marble
        else:
            curr_idx = (curr_idx + 2) % len(marbles)
            if curr_idx == 0:
                marbles.append(marble)
                curr_idx = len(marbles) - 1
            else:
                marbles.insert(curr_idx, marble)

        curr_player = (curr_player + 1) % num_players

    return max(scores.values())


def d9p2(input_text: str):
    # It seems like the naive implementation is too complicated, let's try cleaning up using deque

    num_players, highest_marble = python_utils.parse_ints(input_text)
    highest_marble *= 100
    scores = collections.defaultdict(int)
    marbles = collections.deque([0])
    for marble in range(1, highest_marble):
        if marble % 23 == 0:
            marbles.rotate(7)
            scores[marble % num_players] += marble + marbles.pop()
            # We need an additional rotation to match the logic for next index
            marbles.rotate(-1)
        else:
            marbles.rotate(-1)
            marbles.append(marble)

    return max(scores.values())


if __name__ == '__main__':
    day, year = 9, 2018
    txt = python_utils.get_input(day, year)
    # txt = "13 players; last marble is worth 7999"
    print(f'Part 1: {d9p1(txt)}')
    print(f'Part 2: {d9p2(txt)}')
