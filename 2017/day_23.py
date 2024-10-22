import collections
from typing import List

import python_utils


def d23p1(lines: List[str]):
    registers = collections.defaultdict(int)
    idx = 0
    muls = 0
    while idx < len(lines):
        curr_line = lines[idx]
        ins, op1, op2 = curr_line.strip().split()
        op2 = registers[op2] if op2.isalpha() else int(op2)

        if ins == 'set':
            registers[op1] = op2
        elif ins == 'sub':
            registers[op1] -= op2
        elif ins == 'mul':
            registers[op1] *= op2
            muls += 1
        elif 'jnz' in curr_line and (registers[op1] if op1.isalpha() else int(op1)) != 0:
            idx += op2
            continue

        idx += 1

    return muls


def is_prime(num: int):
    # Special case for 1, 2 and 3
    if num == 1:
        return False
    if num in {2, 3}:
        return True
    if num % 2 == 0:
        return False

    # Check if number is divisible by any odd number between 3 and the square root of num (rounded)
    for div in range(3, int(num ** 0.5) + 1, 2):
        if num % div == 0:
            return False

    return True


def d23p2(lines: List[str]):
    # Today we need to read assembly and translate to a real programming language ;)
    # The solution varies depending on the input, but main concepts are:
    # - "jnz x 2" is the equivalent of a "if x == 0 do next_line"
    # - every jnz x val>2 is a loop
    # - "jnz 1 val" is the equivalent of a while *True* loop containing `val` lines of input
    # - the last "jnz x 2" should execute a "break" for everyone

    # After translating the input it should result in a triple loop that checks if two numbers multiplied are equal to
    # a third number
    # The optimization asks us to understand what problem this code is solving, i.e.:
    # how many composite numbers are there between the initial values of b and c, with a step of 17?
    # Moreover, composite number is the opposite of prime number, hence we implement this
    b = 100 * 81 + 100_000
    c = b + 17_000
    h = 0
    for num in range(b, c + 1, 17):
        if not is_prime(num):
            h += 1

    return h


if __name__ == '__main__':
    day, year = 23, 2017
    lines = python_utils.get_input_as_lines(day, year)
    print(f'Part 1: {d23p1(lines)}')
    print(f'Part 2: {d23p2(lines)}')
