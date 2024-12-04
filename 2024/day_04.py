from typing import List

import python_utils


def d4p1(lines: List[str]):
    # We go with a brute force-ish solution: start from an X and check if any 4 chars in any direction matches XMAS
    grid = {
        (i, j): c
        for i, line in enumerate(lines)
        for j, c in enumerate(line)
    }
    # south, south-west, west, north-west, north, north-east, east, south-east - (y, x) format
    DIRS = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]

    all_xs = [(i, j) for (i, j), c in grid.items() if c == 'X']

    def create_word(grid, start_pos, dir):
        curr = start_pos
        word = ""
        for _ in range(4):
            if curr in grid:
                word += grid[curr]
            else:
                return None
            curr = (curr[0] + dir[0], curr[1] + dir[1])

        return word

    count = 0
    for x_pos in all_xs:
        for dir in DIRS:
            word = create_word(grid, x_pos, dir)
            if word == 'XMAS':
                count += 1

    return count


def d4p2(lines: List[str]):
    # Now we search for an A and we change the check a bit (hard-coded for time reasons)
    grid = {
        (i, j): c
        for i, line in enumerate(lines)
        for j, c in enumerate(line)
    }
    all_as = [(i, j) for (i, j), c in grid.items() if c == 'A']

    count = 0
    for a_pos in all_as:
        y, x = a_pos
        first_diag_pos = [(y - 1, x - 1), a_pos, (y + 1, x + 1)]
        first_diag = ''.join([grid.get(pos, '.') for pos in first_diag_pos])

        second_diag_pos = [(y + 1, x - 1), a_pos, (y - 1, x + 1)]
        second_diag = ''.join([grid.get(pos, '.') for pos in second_diag_pos])

        if first_diag in ['MAS', 'SAM'] and second_diag in ['MAS', 'SAM']:
            count += 1

    return count


if __name__ == '__main__':
    day, year = 4, 2024
    lines = python_utils.get_input_as_lines(day, year)
    print(f'Part 1: {d4p1(lines)}')
    print(f'Part 2: {d4p2(lines)}')
