import itertools
from typing import List

import python_utils


def d24p1(lines: List[str]):
    stones = [python_utils.parse_ints(line) for line in lines]

    # Given a point x0, y0 and a direction vx, vy
    # We use the classic y = mx + q form -- or (y - y0) = m * (x - x0), where m = vy / vx and q = m * x0 + y0
    # Hence we need to ensure that vx is never 0
    # If so we should use a * x + b * y + c = 0
    assert all(vx != 0 for *_, vx, vy, vz in stones)

    stones_eq = [(vy / vx, - vy / vx * px + py) for px, py, _, vx, vy, _ in stones]
    # min_coord, max_coord = 7, 27
    min_coord, max_coord = 200000000000000, 400000000000000

    colliding = 0
    for (i, s1), (j, s2) in itertools.combinations(enumerate(stones), 2):
        m1, q1 = stones_eq[i]
        m2, q2 = stones_eq[j]
        p1x, p1y, _, v1x, v1y, _ = s1
        p2x, p2y, _, v2x, v2y, _ = s2

        # Intersection is found by solving the linear system of equation:
        # y = m1 * x + q1
        # y = m2 * x + q2
        # Its solution is x = (q2 - q1) / (m1 - m2)   --  if m2 != m1
        # Otherwise, they never intersect
        if m1 == m2:
            continue

        x = (q2 - q1) / (m1 - m2)
        y = m1 * x + q1
        future_s1 = (x - p1x) * v1x + (y - p1y) * v1y > 0
        future_s2 = (x - p2x) * v2x + (y - p2y) * v2y > 0
        if future_s1 and future_s2 and min_coord < x < max_coord and min_coord < y < max_coord:
            colliding += 1

    return colliding


def d24p2(lines: List[str]):
    # We hack everything by using sympy :)
    # Simply construct a system of equation with (at least) 3 stones that intersect with the target stone, then solve it

    import sympy

    stones = [python_utils.parse_ints(line) for line in lines]
    sol_x, sol_y, sol_z, sol_vx, sol_vy, sol_vz = sympy.symbols("sx sy sz svx svy svz")
    equations = []
    unk = [sol_x, sol_y, sol_z, sol_vx, sol_vy, sol_vz]
    for i, (px, py, pz, vx, vy, vz) in enumerate(stones[:3]):
        t = sympy.symbols(f"t{i}")
        unk.append(t)
        equations.append(t >= 0)
        equations.append(px + t * vx - sol_x - t * sol_vx)
        equations.append(py + t * vy - sol_y - t * sol_vy)
        equations.append(pz + t * vz - sol_z - t * sol_vz)

    sol = sympy.nonlinsolve(equations, unk)
    return sum(sol.args[0][:3])


if __name__ == '__main__':
    day, year = 24, 2023
    lines = python_utils.get_input_as_lines(day, year)
    print(f'Part 1: {d24p1(lines)}')
    print(f'Part 2: {d24p2(lines)}')
