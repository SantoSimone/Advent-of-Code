from collections import defaultdict
from typing import List

import python_utils


def tree(): return defaultdict(tree)


def d7(lines: List[str]):
    # First of all parse commands into (is_cd, params)
    # i) if cd a -> (True, 'a')
    # ii) if ls + dir e, 120 ff -> (False, [(-1, 'e'), (120, 'ff')])
    commands = []
    i = 0
    while i < len(lines):
        if lines[i].startswith('$ cd'):
            commands.append((True, lines[i][5:]))
            i += 1
        else:
            i += 1
            params = []
            while i < len(lines) and not lines[i].startswith('$'):
                if lines[i].startswith('dir'):
                    params.append((-1, lines[i][4:]))
                else:
                    size, name = lines[i].split(' ')
                    params.append((int(size), name))
                i += 1
            commands.append((False, params))

    # Construct the full tree, not needed but whatever
    fs = tree()
    current = fs
    for is_cd, params in commands:
        if is_cd:
            if params == '..':
                current = current['__parent']
            else:
                current[params]['__parent'] = current
                current[params]['size'] = 0
                current = current[params]
        else:
            for size, name in params:
                if size >= 0:
                    current[name] = size
                else:
                    current[name]['__parent'] = current
                    current[name]['size'] = 0

    # Now compute all sizes, not needed but whatever (plus some python garbage tricks)
    res1 = 0

    def compute_size(curr: tree):
        curr['size'] = sum([x for x in curr.values() if isinstance(x, int)]) + \
                       sum([compute_size(x) for k, x in curr.items() if isinstance(x, dict) and k != "__parent"])
        if curr['size'] < 100000:
            nonlocal res1
            res1 += curr['size']
        return curr['size']

    compute_size(fs)

    # Now let's find the one to delete: compute the needed space to be deleted, find all those that less than requested
    # and take the smallest
    requested = fs['size'] - 40000000
    to_be_evaluated = [fs]
    candidates = []
    while to_be_evaluated:
        eval = to_be_evaluated.pop()
        if eval['size'] > requested:
            candidates.append(eval['size'])
        to_be_evaluated.extend([x for k, x in eval.items() if isinstance(x, dict) and k != "__parent"])

    return res1, min(candidates)


if __name__ == '__main__':
    lines = python_utils.get_input_as_lines(7, 2022)
    print(f"Parts: {d7(lines)}")
