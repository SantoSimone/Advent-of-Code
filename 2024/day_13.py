from typing import List

import sympy

import python_utils


def d13p1(lines: List[str]):
    # There are some equations? Enjoy sympy!

    tokens = 0
    for machine_lines in python_utils.splitter(lines, ''):
        (a_x, a_y), (b_x, b_y), (prize_x, prize_y) = [python_utils.parse_ints(line) for line in machine_lines]
        num_a, num_b = sympy.symbols('num_a num_b')
        eq_x = num_a * a_x + num_b * b_x - prize_x
        eq_y = num_a * a_y + num_b * b_y - prize_y

        sol = sympy.solve([eq_x, eq_y], [num_a, num_b])
        if all(v.is_Integer for v in sol.values()):
            tokens += int(sol[num_a]) * 3 + int(sol[num_b])

    return tokens


def d13p2(lines: List[str]):
    # Since we already used equations for part 1, this is gonna be easy

    tokens = 0
    for machine_lines in python_utils.splitter(lines, ''):
        (a_x, a_y), (b_x, b_y), (prize_x, prize_y) = [python_utils.parse_ints(line) for line in machine_lines]
        num_a, num_b = sympy.symbols('num_a num_b')
        eq_x = num_a * a_x + num_b * b_x - (prize_x + 10_000_000_000_000)
        eq_y = num_a * a_y + num_b * b_y - (prize_y + 10_000_000_000_000)

        sol = sympy.solve([eq_x, eq_y], [num_a, num_b])
        if all(v.is_Integer for v in sol.values()):
            tokens += int(sol[num_a]) * 3 + int(sol[num_b])

    return tokens


if __name__ == '__main__':
    day, year = 13, 2024
    lines = python_utils.get_input_as_lines(day, year)
    print(f'Part 1: {d13p1(lines)}')
    print(f'Part 2: {d13p2(lines)}')
