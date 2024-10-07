import python_utils
from day_10 import d10p2


def d14p1(input_text: str):
    # Simply re-use the hashing from d10 and add the conversion to binary
    used = 0
    for i in range(128):
        for c in d10p2(f"{input_text}-{i}"):
            bin_c = bin(int(c, 16))[2:].zfill(4)
            used += sum(map(int, bin_c))
    return used


def d14p2(input_text: str):
    # Construct the grid, iter over each cell and walk over all adjacent while storing cells visited
    # The number of regions is the number of times we iter over an unvisited cell

    grid = {}
    for i in range(128):
        for stride, c in enumerate(d10p2(f"{input_text}-{i}")):
            bin_c = bin(int(c, 16))[2:].zfill(4)
            for j, b in enumerate(bin_c):
                grid[i, stride * 4 + j] = int(b)

    def neighbours(y: int, x: int):
        return [(y + dy, x + dx) for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]]

    regions = 0
    visited = set()
    for i in range(128):
        for j in range(128):
            if (i, j) in visited:
                continue

            visited.add((i, j))
            if grid[i, j]:
                regions += 1
                q = neighbours(i, j)
                while q:
                    curr = q.pop()
                    if curr in visited:
                        continue
                    visited.add(curr)
                    if grid.get(curr, 0):
                        q.extend(neighbours(*curr))

    return regions


if __name__ == '__main__':
    day, year = 14, 2017
    txt = python_utils.get_input(day, year)
    print(f'Part 1: {d14p1(txt)}')
    print(f'Part 2: {d14p2(txt)}')
