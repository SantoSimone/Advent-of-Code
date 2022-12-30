import operator
import re
from typing import List, Union, Dict, Tuple

import python_utils

OPERATIONS = {
    # Forward op, Reverse op
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv
}


def parse_lines(lines: List[str]):
    monkeys = {}
    for line in lines:
        monkey, other = line.split(':')
        match_int = re.findall(r'\d+', line)
        if len(match_int):
            monkeys[monkey] = int(other.strip())
        else:
            m1, str_op, m2 = re.findall(r'(\w+) ([+\-*/]) (\w+)', other)[0]
            op = OPERATIONS[str_op]
            monkeys[monkey] = (m1, op, m2)

    return monkeys


def solve(monkeys: Dict[str, Union[int, Tuple]], monkey_name: str):
    if type(monkeys[monkey_name]) is int:
        return monkeys[monkey_name]

    m1, op, m2 = monkeys[monkey_name]
    return op(solve(monkeys, m1), solve(monkeys, m2))


def d21p1(lines: List[str]):
    monkeys = parse_lines(lines)
    return solve(monkeys, 'root')


def d21p2(lines: List[str]):
    # Before running this solution you should check that `humn` appears in ONLY one branch of `root`
    monkeys = parse_lines(lines)
    del monkeys["humn"]

    # Find `root`'s branch without `humn`
    root_m1, _, root_m2 = monkeys['root']
    try:
        root_val = solve(monkeys, root_m1)
        to_eval = [root_m2]
    except:
        root_val = solve(monkeys, root_m2)
        to_eval = [root_m1]

    # Reverse all operations while traversing up to `humn`
    while to_eval:
        try:
            m1, op, m2 = monkeys[to_eval.pop()]
        except:  # We hit `humn`
            break

        solved_with_m1 = True
        try:
            eq_val = solve(monkeys, m1)
        except:
            eq_val = solve(monkeys, m2)
            solved_with_m1 = False

        if op == operator.sub:
            if solved_with_m1:
                # root = a - b and we know a --> b = a - root (b != 0)
                root_val = eq_val - root_val
            else:
                # root = a - b and we know b --> a = root + b
                root_val = root_val + eq_val
        elif op == operator.floordiv:
            if solved_with_m1:
                # root = a / b and we know a --> b = root/a (b != 0)
                root_val = root_val / eq_val
            else:
                # root = a / b and we know b --> a = root * b
                root_val = root_val * eq_val
        elif op == operator.add:
            root_val = root_val - eq_val
        else:  # op == operator.mul
            root_val = root_val // eq_val

        to_eval.append(m2 if solved_with_m1 else m1)

    return root_val


if __name__ == '__main__':
    lines = python_utils.get_input_as_lines(21, 2022)
    print(f"Part 1: {d21p1(lines)}")
    print(f"Part 2: {d21p2(lines)}")
