import collections
import re
from typing import List, Tuple

import python_utils


def part_condition(c: str) -> bool:
    return not c.isdigit() and c != '.'


def find_parts_with_adj_symbols(lines: List[str]) -> List[Tuple[int, int, int, int]]:
    parts_with_symbols = []

    for i, line in enumerate(lines):
        part_matches = re.finditer(r'\d+', line)
        for match in part_matches:
            start = match.span()[0]
            end = match.span()[1]

            if (
                    # check line before
                    (i > 0 and any(part_condition(c) for c in lines[i - 1][max(start - 1, 0):end + 1])) or
                    # check line after
                    (i + 1 < len(lines) and any(part_condition(c) for c in lines[i + 1][max(start - 1, 0):end + 1])) or
                    start - 1 > 0 and part_condition(line[start - 1]) or  # check left of current line
                    end < len(line) and part_condition(line[end])  # check right of current line
            ):
                parts_with_symbols.append((int(line[start:end]), i, start, end))

    return parts_with_symbols


def d3p1(lines: List[str]):
    parts = find_parts_with_adj_symbols(lines)

    return sum([p for p, *_ in parts])


def d3p2(lines: List[str]):
    parts = find_parts_with_adj_symbols(lines)

    candidate_gears = collections.defaultdict(list)
    for part, line_idx, part_start, part_end in parts:
        # check line before
        if line_idx > 0:
            gear_idx = lines[line_idx - 1][max(part_start - 1, 0):part_end + 1].find(r'*')
            if gear_idx > -1:
                candidate_gears[line_idx - 1, max(part_start - 1, 0) + gear_idx].append(part)
        # check line after
        if line_idx < len(lines) - 1:
            gear_idx = lines[line_idx + 1][max(part_start - 1, 0):part_end + 1].find(r'*')
            if gear_idx > -1:
                candidate_gears[line_idx + 1, max(part_start - 1, 0) + gear_idx].append(part)
        # check left
        if part_start > 1 and lines[line_idx][part_start - 1] == '*':
            candidate_gears[line_idx, part_start - 1].append(part)
        # check right
        if part_end < len(lines[line_idx]) - 1 and lines[line_idx][part_end] == '*':
            candidate_gears[line_idx, part_end].append(part)

    gear_ratios = [
        parts[0] * parts[1]
        for candidate, parts in candidate_gears.items()
        if len(parts) == 2
    ]

    return sum(gear_ratios)


if __name__ == '__main__':
    lines = python_utils.get_input_as_lines(3, 2023)
    print(f"Part 1: {d3p1(lines)}")
    print(f"Part 2: {d3p2(lines)}")
