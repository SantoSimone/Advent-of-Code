from collections import deque

import python_utils


def d6p1(data: str):
    window = deque(data[:4])
    pos = 4
    for c in data[4:]:
        if len(set(window)) == 4:
            return pos
        window.popleft()
        window.append(c)
        pos += 1

    return -1


def d6p2(data: str):
    window = deque(data[:14])
    pos = 14
    for c in data[14:]:
        if len(set(window)) == 14:
            return pos
        window.popleft()
        window.append(c)
        pos += 1

    return -1


if __name__ == '__main__':
    data = python_utils.get_input(6, 2022)
    # data = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
    print(f"Part 1: {d6p1(data)}")
    print(f"Part 2: {d6p2(data)}")
