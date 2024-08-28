import collections
import re
from typing import List

import python_utils


def d4p1(lines: List[str]):
    valid = 0
    for line in lines:
        counter = collections.Counter(re.findall('\w+', line))
        if counter.most_common(1)[0][1] == 1:
            valid += 1
    return valid


def d4p2(lines: List[str]):
    valid = 0
    for line in lines:
        sorted_words = set()
        for word in re.findall('\w+', line):
            sorted_word = ''.join(sorted(word))
            if sorted_word in sorted_words:
                break
            sorted_words.add(sorted_word)
        else:
            valid += 1

    return valid


if __name__ == '__main__':
    day, year = 4, 2017
    lines = python_utils.get_input_as_lines(day, year)
    print(f'Part 1: {d4p1(lines)}')
    print(f'Part 2: {d4p2(lines)}')
