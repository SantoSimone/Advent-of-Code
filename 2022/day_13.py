import functools
import itertools
import json
from typing import List, Union

import python_utils


def compare(lhs: Union[int, List], rhs: Union[int, List]) -> int:
    """Return negative if lhs < rhs, 0 if lhs == rhs, positive if lhs > rhs"""
    if type(lhs) == type(rhs) == int:
        return lhs - rhs

    if type(lhs) != list:
        lhs = [lhs]
    if type(rhs) != list:
        rhs = [rhs]

    for l, r in zip(lhs, rhs):
        res = compare(l, r)
        if res != 0:
            return res

    return len(lhs) - len(rhs)


def d13p1(lines: List[str]):
    all_pairs = python_utils.splitter(lines, "")
    count = 0
    for i, pair in enumerate(all_pairs):
        # Enjoy the one liner parsing
        p1 = json.loads(pair[0])
        p2 = json.loads(pair[1])
        ordered = True
        for v1, v2 in zip(p1, p2):
            res = compare(v1, v2)
            if res > 0:
                ordered = False
            if res != 0:
                break
        else:
            ordered = len(p1) < len(p2)

        # indices.append(i if ordered else None)
        count += (i + 1) if ordered else 0

    return count


def d13p2(lines: List[str]):
    # TIL cmp_to_key, python standard packages are insane
    all_pairs = python_utils.splitter(lines, "")
    all_pairs = [json.loads(p) for p in itertools.chain(*all_pairs)]
    all_pairs += [[[2]], [[6]]]
    all_pairs.sort(key=functools.cmp_to_key(compare))
    return (all_pairs.index([[2]]) + 1) * (all_pairs.index([[6]]) + 1)


if __name__ == '__main__':
    lines = python_utils.get_input_as_lines(13, 2022)
    print(f"Part 1: {d13p1(lines)}")
    print(f"Part 2: {d13p2(lines)}")
