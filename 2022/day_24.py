from typing import List, Tuple

import python_utils

BLIZZARD_MOVES = {
    # Type, (row_move, col_move)
    '>': (0, 1),
    '<': (0, -1),
    '^': (-1, 0),
    'v': (1, 0)
}


def parse_grid(lines: List[str]) -> Tuple[Tuple[int, int],
                                          Tuple[int, int],
                                          List[Tuple[Tuple[int, int], Tuple[int, int]]]]:
    start = (0, next(i for i, ch in enumerate(lines[0]) if ch != '#'))
    end = (len(lines) - 1, next(i for i, ch in enumerate(lines[-1]) if ch != '#'))
    blizzards = []
    for r, line in enumerate(lines):
        for c, ch in enumerate(line):
            if ch in BLIZZARD_MOVES.keys():
                blizzards.append(((r, c), BLIZZARD_MOVES[ch]))

    return start, end, blizzards


def from_to(start: Tuple[int, int], end: Tuple[int, int], blizzards: List[Tuple[Tuple[int, int], Tuple[int, int]]],
            height: int, width: int):
    to_eval = {start}
    moves = 0
    while end not in to_eval:
        # -1 / +1 trick for module in range [1, N] instead of [0, N-1]
        # Also, height and width need to be adjusted for "#" characters in `lines`
        blizzards = [
            (((blizz_r + move_r - 1) % (height - 2) + 1,
              (blizz_c + move_c - 1) % (width - 2) + 1),
             (move_r, move_c))
            for (blizz_r, blizz_c), (move_r, move_c) in blizzards
        ]

        new_eval = set()
        for r, c in to_eval:
            for add_r, add_c in [(0, 1), (0, -1), (-1, 0), (1, 0), (0, 0)]:
                new_r, new_c = r + add_r, c + add_c

                # width - 1 to account for "#" characters in `lines`
                if new_r < 0 or new_r >= height or new_c <= 0 or new_c >= width - 1:
                    continue

                if (new_r, new_c) in [(br, bc) for (br, bc), (_, _) in blizzards]:
                    continue
                if new_r == 0 and (new_r, new_c) not in [start, end]:
                    continue
                if new_r == height - 1 and (new_r, new_c) not in [start, end]:
                    continue

                new_eval.add((new_r, new_c))

        moves += 1

        to_eval = new_eval.copy()

    return moves, blizzards


def d24p1(lines: List[str]):
    # Slow solution... STILL A SOLUTION
    start, end, blizzards = parse_grid(lines)
    height, width = len(lines), len(lines[0])
    return from_to(start, end, blizzards, height, width)[0]


def d24p2(lines: List[str]):
    # Slow solution... STILL A SOLUTION
    start, end, blizzards = parse_grid(lines)
    height, width = len(lines), len(lines[0])
    p1, blizzards = from_to(start, end, blizzards, height, width)
    p2, blizzards = from_to(end, start, blizzards, height, width)
    p3, blizzards = from_to(start, end, blizzards, height, width)
    return p1 + p2 + p3


if __name__ == '__main__':
    # Definitely needs speed up
    lines = python_utils.get_input_as_lines(24, 2022)
    print(f"Part 1: {d24p1(lines)}")
    print(f"Part 2: {d24p2(lines)}")
