import collections
import operator
import re
from typing import List

import python_utils


def parse_workflows(lines: List[str]):
    workflows = collections.defaultdict(list)
    for line in lines:
        name, rules = re.match(r'(\w+){(.+)}', line).groups()
        for rule in rules.split(','):
            splits = rule.split(':')
            if len(splits) == 1:
                workflows[name].append((True, splits[0]))
            else:
                attr, op, val = re.match(r'(x|m|a|s)(<|>)(\d+)', splits[0]).groups()
                op = operator.gt if op == '>' else operator.lt
                workflows[name].append(((attr, op, int(val)), splits[1]))

    return workflows


def d19p1(lines: List[str]):
    workflows_lines, parts_lines = python_utils.splitter(lines, '')
    workflows = parse_workflows(workflows_lines)
    parts = [{k: int(v) for k, v in re.findall(r'(x|m|a|s)=(\d+)', line)} for line in parts_lines]
    res = []
    for part in parts:
        curr_workflow = "in"
        while not (curr_workflow in ['A', 'R']):
            for rule, next_wf in workflows[curr_workflow]:
                if rule == True:
                    curr_workflow = next_wf
                    break

                attr, op, val = rule
                if op(part[attr], val):
                    curr_workflow = next_wf
                    break

        res.append(curr_workflow)

    return sum(sum(part.values()) for i, part in enumerate(parts) if res[i] == 'A')


def d19p2(lines: List[str]):
    # Cut ranges everytime a rule is applied, then update current range and go on
    workflows_lines, parts_lines = python_utils.splitter(lines, '')
    workflows = parse_workflows(workflows_lines)

    ranges = [({v: (1, 4000) for v in 'xmas'}, 'in')]
    total = 0
    while ranges:
        curr_range, curr_workflow = ranges.pop()

        if curr_workflow == 'R':
            continue

        if curr_workflow == 'A':
            total += python_utils.multiply([hi - lo + 1 for lo, hi in curr_range.values()])

        for rule, next_wf in workflows[curr_workflow]:
            if rule == True:
                ranges.append(({k: v for k, v in curr_range.items()}, next_wf))
                continue

            attr, op, val = rule
            lo, hi = curr_range[attr]
            if op == operator.lt:
                if lo < val:
                    ranges.append((curr_range | {attr: (lo, val - 1)}, next_wf))
                curr_range[attr] = (max(val, lo), hi)
            else:
                if hi > val:
                    ranges.append((curr_range | {attr: (val + 1, hi)}, next_wf))
                curr_range[attr] = (lo, min(val, hi))

    return total


if __name__ == '__main__':
    day, year = 19, 2023
    lines = python_utils.get_input_as_lines(day, year)
    print(f'Part 1: {d19p1(lines)}')
    print(f'Part 2: {d19p2(lines)}')
