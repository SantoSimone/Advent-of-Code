import re
from typing import List, Tuple

import numpy as np

from python_utils import get_input_as_lines, splitter, parse_ints


def parse_inputs(lines: List[str]) -> Tuple[map, List[np.ndarray]]:
    drawn_numbers = parse_ints(lines[0])
    boards = splitter(lines[2:], '')
    boards = [
        np.array(
            [parse_ints(line) for line in board]
        )
        for board in boards
    ]

    return drawn_numbers, boards


def check_board(board: np.array, moves: List[int]):
    # Check rows
    col_completed = any(
        all(x in moves for x in board[:, c])
        for c in range(board.shape[1])
    )
    row_completed = any(
        all(x in moves for x in board[c, :])
        for c in range(board.shape[0])
    )
    return row_completed or col_completed


def d4p1(lines: List[str]):
    drawn_numbers, boards = parse_inputs(lines)

    for i, num in enumerate(drawn_numbers):
        for board in boards:
            if check_board(board, drawn_numbers[:i + 1]):
                num_unchecked = sum(set(board.ravel()).difference(drawn_numbers[:i + 1]))
                return num_unchecked * num

    return 0


def d4p2(lines: List[str]):
    drawn_numbers, boards = parse_inputs(lines)
    already_won = [False] * len(boards)

    for i, num in enumerate(drawn_numbers):
        for board_num, board in enumerate(boards):
            if already_won[board_num]:
                continue

            if check_board(board, drawn_numbers[:i + 1]):
                if np.sum(already_won) == len(boards) - 1:
                    num_unchecked = sum(set(board.ravel()).difference(drawn_numbers[:i + 1]))
                    return num_unchecked * num
                else:
                    already_won[board_num] = True

    return 0


if __name__ == '__main__':
    lines = get_input_as_lines(4, 2021)
    print(f"Part 1: {d4p1(lines)}")
    print(f"Part 2: {d4p2(lines)}")
