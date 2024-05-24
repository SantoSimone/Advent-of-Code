import collections
import re
from typing import List

import python_utils


def count_card_matches(line: str) -> int:
    _, numbers = line.split(':')
    winning, mine = [re.findall(r'\d+', split) for split in numbers.split('|')]
    matches = [num in winning for num in mine]
    return sum(matches)


def d4p1(lines: List[str]):
    match_count = [count_card_matches(line) for line in lines]
    card_values = [int(2 ** (count - 1)) for count in match_count]

    return sum(card_values)


def d4p2(lines: List[str]):
    match_count = [count_card_matches(line) for line in lines]
    card_count = collections.defaultdict(lambda: 1, {i: 1 for i in range(1, len(match_count) + 1)})

    for card_num, matches in enumerate(match_count[:-1], 1):
        for copy_num in range(card_num + 1, card_num + matches + 1):
            card_count[copy_num] += 1 * card_count[card_num]

    return sum(card_count.values())


if __name__ == '__main__':
    day, year = 4, 2023
    lines = python_utils.get_input_as_lines(day, year)
    print(f"Part 1: {d4p1(lines)}")
    print(f"Part 2: {d4p2(lines)}")
