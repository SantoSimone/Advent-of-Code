from typing import List
import python_utils


def d10p1(lines: List[str]):
    numbers = [
        int(line.split(' ')[1]) if line.startswith('addx') else 0
        for line in lines
    ]

    X = 1
    cycle = 0
    waypoints = range(20, 221, 40)
    signals = []
    for number in numbers:
        for sub in range(2 if number != 0 else 1):
            cycle += 1
            if cycle in waypoints:
                signals.append(cycle * X)
            X += number if sub > 0 else 0

    return sum(signals)


def d10p2(lines: List[str]):
    numbers = [
        int(line.split(' ')[1]) if line.startswith('addx') else 0
        for line in lines
    ]

    X = 1
    canvas = [0] * 240
    cycle = -1
    for number in numbers:
        for sub in range(2 if number != 0 else 1):
            cycle += 1
            canvas[cycle] = 1 if abs(X - (cycle % 40)) <= 1 else 0
            X += number if sub > 0 else 0

    for r in range(6):
        print(''.join(['#' if x else '.' for x in canvas[r * 40: (r + 1) * 40]]))


if __name__ == '__main__':
    lines = python_utils.get_input_as_lines(10, 2022)
    print(f"Part 1: {d10p1(lines)}")
    d10p2(lines)
