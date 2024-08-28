import python_utils


def d3p1(input_text: str):
    # We loop the increasing squares of the spirals, i.e. first square is 1x1, second square is 3x3, third is 5x5 etc.
    # We loop until the highest number covered in the outer side of the current square is higher than the target number
    # Than we look for the shortest path, i.e. distance to the closest middle point of each side plus side's half-length

    target = int(input_text)
    curr_side = 1
    while True:
        curr_max_num = curr_side ** 2
        if curr_max_num > target:
            bottom_side_middle = curr_max_num - curr_side // 2
            left_side_middle = bottom_side_middle - curr_side + 1
            top_side_middle = left_side_middle - curr_side + 1
            right_side_middle = top_side_middle - curr_side + 1
            closest_middle_distance = min([abs(target - m) for m in
                                           [bottom_side_middle, left_side_middle, right_side_middle, top_side_middle]])
            path = closest_middle_distance + curr_side // 2
            break

        curr_side += 2

    return path


def next_step(x: int, y: int):
    if x == y == 0:
        return 1, 0
    elif -x < y < x:
        return x, y + 1
    elif y > -x and y >= x:
        return x - 1, y
    elif -x >= y > x:
        return x, y - 1
    elif y <= -x and x >= y:
        return x + 1, y
    return None


def d3p2(input_text: str):
    # Now we need to build the spiral (unluckily)

    target = int(input_text)
    x = y = 0
    grid = {(0, 0): 1}
    while grid[x, y] < target:
        x, y = next_step(x, y)
        grid[x, y] = sum(grid.get((x + dx, y + dy), 0) for dx in [0, 1, -1] for dy in [0, 1, -1])

    return grid[x, y]


if __name__ == '__main__':
    day, year = 3, 2017
    txt = python_utils.get_input(day, year)
    print(f'Part 1: {d3p1(txt)}')
    print(f'Part 2: {d3p2(txt)}')
