import collections
from typing import List, Dict

import python_utils


def tree(): return collections.defaultdict(tree)


class Node:
    num_child: int
    meta: List[int]


def process_single(idx: int, nums: List[int], tree_root: Dict):
    num_child, num_meta = nums[idx:idx + 2]
    idx += 2

    for i in range(num_child):
        idx = process_single(idx, nums, tree_root[i])
        # tree_root[start_idx]['children'].append(child)

    tree_root['metadata'] = nums[idx:idx + num_meta]
    idx += num_meta

    return idx


def d8p1(input_text: str):
    # Embrace recursion

    nums = python_utils.parse_ints(input_text)

    root = tree()
    process_single(0, nums, root)

    sum_meta = 0

    def compute_meta(node: Dict):
        nonlocal sum_meta
        if 'metadata' in node:
            sum_meta += sum(node['metadata'])
        for k in node.keys():
            if k != 'metadata':
                compute_meta(node[k])

    compute_meta(root)
    return sum_meta


def d8p2(input_text: str):
    nums = python_utils.parse_ints(input_text)

    root = tree()
    process_single(0, nums, root)

    def give_scores(node: Dict):
        if any(type(k) == int for k in node.keys()):
            for c in node['metadata']:
                give_scores(node[c - 1])
            node['score'] = sum(node[c - 1]['score'] for c in node['metadata'])
        else:
            node['score'] = sum(node['metadata'])

    give_scores(root)
    return root['score']


if __name__ == '__main__':
    day, year = 8, 2018
    txt = python_utils.get_input(day, year)
    print(f'Part 1: {d8p1(txt)}')
    print(f'Part 2: {d8p2(txt)}')
