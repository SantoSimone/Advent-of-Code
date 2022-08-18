import collections
import functools
import itertools
import random
import re
from typing import Tuple, List

import numpy as np

from python_utils import get_input, get_input_as_lines, splitter

"""
This day is a bit of a reverse-engineering problem, so I will put all my thoughts here at the start, solution is based 
on this obviously.

- We have 14 block of instructions
- Blocks can be divided in two types, based on the `div z N` instruction, where N can be 1 or 26
- Blocks can be summarized as the following formula: block = f(z, w, eq, a, b)
  - z is the variable we are tracking
  - w is the input digit (total 14)
  - eq is either 1 or 0, based on the result of `z % 26 + a != w`
  - a and b are two values that vary at every block, e.g. 
        inp w
        mul x 0
        add x z
        mod x 26
        div z 1
        add x 10 (a = 10)
        eql x w
        eql x 0
        mul y 0
        add y 25
        mul y x
        add y 1
        mul z y
        mul y 0
        add y w
        add y 12 (b = 12)
        mul y x
        add z y
- Blocks `div z 1` output is:
  - 26 * z + w + b  if eq == 1
  - z               if eq == 0
- Blocks `div z 26` output is:
  - z // 26                 if eq == 1
  - 26 * (z // 26) + w + b  if eq == 0
- z is always non-negative, so for `div z 1` blocks eq = 1 always
- The final value of z should be 0
- If every block `div z 1` gives 26z + something, so every block `div z 26` _should_ give z // 26
  - This creates the constraints of our problem: we need eq = 1, therefore `z % 26 + a == w`
  - But since `div z 1` gives 26z + something AND the equality uses z % 26, we are actually doing `something == w - a`
  - So at each `div z 26` block we create a constraint between last `div z 1` block's `w + b` value (= z % 26 in current 
    block) and `w - a` of the current `div z 26` block  
  - This constraints will solve the problem
- I will produce one function that prints the constraints and then figure out the MONAD by hand (I spent too much time 
  on this problem already)
"""


def print_constraints(lines: List[str]):
    groups = splitter(lines, "inp w")[1:]
    outputs = []
    constraints = []

    for i, g in enumerate(groups):
        instructions = [line.split(" ") for line in g]
        type = int(instructions[3][2])
        a = int(instructions[4][2])
        b = int(instructions[-3][2])
        print(f"Group {i} - Type {type}")
        print(f"a = {a}")
        print(f"b = {b}")

        if type == 1:
            outputs.append([f"w{i}", b])
        else:
            w, b = outputs.pop()
            constraints.append(f"w{i} == {w} + {b + a}")
    print(constraints)
    # Resulting constraints were
    #   monad[5] == monad[4]
    #   monad[7] == monad[6] - 4
    #   monad[8] == monad[3] - 1
    #   monad[10] == monad[9] + 7
    #   monad[11] == monad[2] - 6
    #   monad[12] == monad[1] + 6
    #   monad[13] == monad[0] + 4


if __name__ == '__main__':
    lines = get_input_as_lines(24, 2021)
    print_constraints(lines)
    print(f"Part 1: 53999995829399")
    print(f"Part 2: 11721151118175")
