from typing import List
import python_utils


def d1p1(lines: List[str]):
    splitted = python_utils.splitter(lines, "")
    elves = [map(int, s) for s in splitted]
    return max([sum(elf) for elf in elves])


def d1p2(lines:List[str]):
    splitted = python_utils.splitter(lines, "")
    elves = [map(int, s) for s in splitted]
    elves_sum = sorted([sum(elf) for elf in elves], reverse=True)
    return sum(elves_sum[:3])


if __name__ == '__main__':
    lines = python_utils.get_input_as_lines(1, 2022)
    print(f"Part 1: {d1p1(lines)}")
    print(f"Part 2: {d1p2(lines)}")
