import collections
import operator
from typing import List, Tuple, Callable

import python_utils

OPERATORS = {
    '<': operator.lt,
    '<=': operator.le,
    '>': operator.gt,
    '>=': operator.ge,
    '==': operator.eq,
    '!=': operator.ne
}


def parse_inputs(lines: List[str]) -> List[Tuple[str, Callable, int, str, Callable, int]]:
    instructions = []
    for line in lines:
        chunks = line.split()
        reg = chunks[0]
        op = operator.add if chunks[1] == "inc" else operator.sub
        qty = int(chunks[2])
        reg_cond = chunks[4]
        op_cond = OPERATORS[chunks[5]]
        qty_cond = int(chunks[6])
        instructions.append((reg, op, qty, reg_cond, op_cond, qty_cond))

    return instructions


def d8p1(lines: List[str]):
    instructions = parse_inputs(lines)

    registers = collections.defaultdict(int)
    for reg, op, qty, reg_cond, op_cond, qty_cond in instructions:
        if op_cond(registers[reg_cond], qty_cond):
            registers[reg] = op(registers[reg], qty)

    return registers[max(registers, key=registers.__getitem__)]


def d8p2(lines: List[str]):
    instructions = parse_inputs(lines)
    max_val = 0

    registers = collections.defaultdict(int)
    for reg, op, qty, reg_cond, op_cond, qty_cond in instructions:
        if op_cond(registers[reg_cond], qty_cond):
            registers[reg] = op(registers[reg], qty)
            if registers[reg] > max_val:
                max_val = registers[reg]

    return max_val


if __name__ == '__main__':
    day, year = 8, 2017
    lines = python_utils.get_input_as_lines(day, year)
    print(f'Part 1: {d8p1(lines)}')
    print(f'Part 2: {d8p2(lines)}')
