import functools
import operator
import re
from collections import deque
from typing import List

import python_utils


class Monkey:
    def __init__(self):
        self.items = deque()
        self.operation = operator.add
        self.factor = 0
        self.test = 0
        self.true_val = 0
        self.false_val = 0
        self.count = 0


def parse_inputs(lines: List[str]) -> List[Monkey]:
    monkeys = []
    idx = 1
    curr = Monkey()
    while idx < len(lines):
        if lines[idx].startswith('Monkey'):
            monkeys.append(curr)
            curr = Monkey()

        if lines[idx].strip().startswith('Starting items'):
            curr.items.extend(list(map(int, re.findall(r'\d+', lines[idx]))))

        if lines[idx].strip().startswith('Operation'):
            splits = lines[idx].split(' ')
            curr.operation = operator.add if splits[-2] == '+' else operator.mul
            curr.factor = -1 if splits[-1] == 'old' else int(splits[-1])

        if lines[idx].strip().startswith('Test'):
            curr.test = int(re.findall(r'\d+', lines[idx])[0])

        if lines[idx].strip().startswith('If true'):
            curr.true_val = int(re.findall(r'\d+', lines[idx])[0])

        if lines[idx].strip().startswith('If false'):
            curr.false_val = int(re.findall(r'\d+', lines[idx])[0])

        idx += 1
    monkeys.append(curr)
    return monkeys


def d11p1(lines: List[str]):
    monkeys = parse_inputs(lines)
    for i in range(20):
        for monkey in monkeys:
            while monkey.items:
                item = monkey.items.popleft()
                item = monkey.operation(item, item if monkey.factor == -1 else monkey.factor) // 3
                if (item % monkey.test) == 0:
                    monkeys[monkey.true_val].items.append(item)
                else:
                    monkeys[monkey.false_val].items.append(item)
                monkey.count += 1

    monkeys_sorted = sorted(monkeys, key=lambda m: m.count, reverse=True)
    return monkeys_sorted[0].count * monkeys_sorted[1].count


def d11p2(lines: List[str]):
    monkeys = parse_inputs(lines)
    divider = functools.reduce(operator.mul, [m.test for m in monkeys])
    for i in range(10000):
        for monkey in monkeys:
            while monkey.items:
                item = monkey.items.popleft()
                item = monkey.operation(item, item if monkey.factor == -1 else monkey.factor) % divider
                if (item % monkey.test) == 0:
                    monkeys[monkey.true_val].items.append(item)
                else:
                    monkeys[monkey.false_val].items.append(item)
                monkey.count += 1

    monkeys_sorted = sorted(monkeys, key=lambda m: m.count, reverse=True)
    return monkeys_sorted[0].count * monkeys_sorted[1].count


if __name__ == '__main__':
    lines = python_utils.get_input_as_lines(11, 2022)
    print(f"Part 1: {d11p1(lines)}")
    print(f"Part 2: {d11p2(lines)}")
