from typing import List

import python_utils


def d16p1(input_text: str):
    letters = list('abcdefghijklmnop')
    letters = dance_once(letters, input_text)

    return ''.join(letters)


def dance_once(letters: List[str], input_text: str) -> List[str]:
    for move in input_text.split(','):
        if move[0] == 's':
            span = python_utils.parse_ints(move)[0]
            letters = letters[-span:] + letters[:len(letters) - span]
        elif move[0] == 'x':
            i1, i2 = python_utils.parse_ints(move)
            letters[i1], letters[i2] = letters[i2], letters[i1]
        elif move[0] == 'p':
            i1 = letters.index(move[1])
            i2 = letters.index(move[3])
            letters[i1], letters[i2] = letters[i2], letters[i1]

    return letters


def d16p2(input_text: str):
    # It must repeat somewhere
    letters = list('abcdefghijklmnop')

    seen = {tuple(letters): 0}
    for i in range(1_000_000_000):
        letters = dance_once(letters, input_text)
        if tuple(letters) in seen:
            break
        else:
            seen[tuple(letters)] = i

    start_loop = seen[tuple(letters)]
    loop_length = i - start_loop + 1
    remaining = (1_000_000_000 - start_loop) % loop_length
    for _ in range(remaining):
        letters = dance_once(letters, input_text)

    return ''.join(letters)


if __name__ == '__main__':
    day, year = 16, 2017
    txt = python_utils.get_input(day, year)
    print(f'Part 1: {d16p1(txt)}')
    print(f'Part 2: {d16p2(txt)}')
