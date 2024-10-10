import python_utils


def d17p1(input_text: str):
    step = int(input_text)
    buffer = [0]
    curr_idx = 0
    for i in range(1, 2018):
        insert_idx = (curr_idx + step) % len(buffer) + 1
        buffer.insert(insert_idx, i)
        curr_idx = insert_idx

    return buffer[(buffer.index(2017) + 1) % len(buffer)]


def d17p2(input_text: str):
    # The trick is that everything is added AFTER the current index and 0 is at the first index, hence we only need to
    # keep track of the last time the insert_idx is 0, avoiding manipulating the array 50_000_000 times
    step = int(input_text)
    curr_idx = 0
    last = 0
    for i in range(1, 50_000_000):
        curr_idx = (curr_idx + step) % i + 1
        if curr_idx == 1:
            last = i

    return last


if __name__ == '__main__':
    day, year = 17, 2017
    txt = python_utils.get_input(day, year)
    print(f'Part 1: {d17p1(txt)}')
    print(f'Part 2: {d17p2(txt)}')
