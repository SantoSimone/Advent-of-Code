import itertools
import re
from typing import List, Dict
from python_utils import get_input_as_lines


def count_in_line(line: str) -> int:
    inputs = re.findall(r'\w+', line)
    pre_delimiter, post_delimiter = inputs[:10], inputs[10:]
    count = 0
    for seq in post_delimiter:
        if len(seq) in [2, 3, 4, 7]:
            count += 1

    return count


def d8p1(lines: List[str]):
    return sum([count_in_line(line) for line in lines])


def get_dict(pre: List[str]) -> Dict[str, str]:
    # Brute force, try all possible dicts and check validity
    original_mapping = {
        0: 'abcefg',
        1: 'cf',
        2: 'acdeg',
        3: 'acdfg',
        4: 'bcdf',
        5: 'abdfg',
        6: 'abdefg',
        7: 'acf',
        8: 'abcdefg',
        9: 'abcdfg',
    }

    for p in itertools.permutations('abcdefg'):
        mapping = dict(zip(p, 'abcdefg'))
        reverse_map = {b: a for a, b in mapping.items()}
        possible = True

        for seq in pre:
            if not possible:
                break
            seq_perm = ''.join([mapping[c] for c in seq])
            if ''.join(sorted(seq_perm)) not in original_mapping.values():
                possible = False

        if possible:
            # If permutation is compliant we return the mapping num <-> string
            ret_mapping = {}
            for i in range(0, 10):
                ret_mapping[''.join(sorted([reverse_map[c] for c in original_mapping[i]]))] = str(i)

            return ret_mapping


def solve_line(line: str) -> int:
    inputs = re.findall(r'\w+', line)
    pre_delimiter, post_delimiter = inputs[:10], inputs[10:]

    current_mapping = get_dict(pre_delimiter)

    four_digits = ''.join([current_mapping[''.join(sorted(val))] for val in post_delimiter])
    return int(four_digits)


def d8p2(lines: List[str]):
    return sum([solve_line(line) for line in lines])


if __name__ == '__main__':
    lines = get_input_as_lines(8, 2021)
    # lines = ["acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"]
    print(f"Part 1: {d8p1(lines)}")
    print(f"Part 2: {d8p2(lines)}")
