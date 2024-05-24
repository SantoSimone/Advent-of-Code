import collections
import re
from typing import List

import numpy as np

import python_utils


def parse_games(lines: List[str]):
    games = []
    for line in lines:
        game_string, cubes_string = line.split(':')
        games.append([
            {
                cubes_color: int(cubes_num)
                for _, cubes_num, cubes_color in re.findall(r'((\d+) (blue|red|green))+', cubes_set)
            }
            for cubes_set in cubes_string.strip().split(';')
        ])

    return games


def d2p1(lines: List[str]):
    # Too much nested loops
    games = parse_games(lines)
    max_cubes = {'red': 12, 'green': 13, 'blue': 14}

    possible_game_ids = []
    for i, game in enumerate(games):
        should_add = True
        for cubes_set in game:
            if any(cube_num > max_cubes[cube_color] for cube_color, cube_num in cubes_set.items()):
                should_add = False
                break

        if should_add:
            possible_game_ids.append(i + 1)

    return sum(possible_game_ids)


def d2p2(lines: List[str]):
    games = parse_games(lines)

    game_powers = []
    for game in games:
        max_dict = collections.defaultdict(int)
        for cubes_set in game:
            for cube_color, cube_num in cubes_set.items():
                max_dict[cube_color] = max(max_dict[cube_color], cube_num)

        game_powers.append(np.prod(list(max_dict.values())))

    return sum(game_powers)


if __name__ == '__main__':
    lines = python_utils.get_input_as_lines(2, 2023)
    print(f"Part 1: {d2p1(lines)}")
    print(f"Part 2: {d2p2(lines)}")
