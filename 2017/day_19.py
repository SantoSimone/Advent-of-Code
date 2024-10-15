from pathlib import Path
from typing import List, Tuple, Dict


def parse_inputs(lines: List[str]) -> Dict[Tuple[int, int], str]:
    grid = {}
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            grid[i, j] = c

    return grid


def get_curr_dirs(char: str, last_dir: Tuple[int, int]):
    if char == '|':
        return [(-1, 0), (1, 0)] if last_dir[0] != 0 else [(0, -1), (0, 1)]
    elif char == '-':
        return [(0, -1), (0, 1)] if last_dir[1] != 0 else [(-1, 0), (1, 0)]
    elif char == '+':
        return [(-1, 0), (1, 0), (0, -1), (0, 1)]

    return []


def d19(lines: List[str]):
    grid = parse_inputs(lines)
    start = next((i, j) for (i, j), c in grid.items() if i == 0 and c != ' ')
    visited = set()
    q = [((start[0] + i, start[1] + j), (i, j), 1) for i, j in get_curr_dirs(grid[start], (1, 0))]
    last_char_at = -1
    collected = ''

    while q:
        curr_pos, last_dir, steps = q.pop()

        if not (0 <= curr_pos[0] < len(lines) and 0 <= curr_pos[1] <= len(lines[0])):
            continue
        if (curr_pos, abs(last_dir[0]), abs(last_dir[1])) in visited:
            continue

        visited.add((curr_pos, abs(last_dir[0]), abs(last_dir[1])))

        if grid[curr_pos].isalpha():
            collected += grid[curr_pos]
            last_char_at = steps
            q.append(((curr_pos[0] + last_dir[0], curr_pos[1] + last_dir[1]), last_dir, steps + 1))

        possible_dir = get_curr_dirs(grid[curr_pos], last_dir)
        for next_dir in possible_dir:
            q.append(((curr_pos[0] + next_dir[0], curr_pos[1] + next_dir[1]), next_dir, steps + 1))

    return collected, last_char_at + 1


if __name__ == '__main__':
    day, year = 19, 2017
    with open(Path(__file__).parent / "input_files" / f"input{day}.txt", 'r') as input_file:
        lines = input_file.read().splitlines()
    p1, p2 = d19(lines)
    print(f'Part 1: {p1}')
    print(f'Part 2: {p2}')
