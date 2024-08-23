import python_utils


def d1p1(input_text: str):
    numbers = list(map(int, input_text))

    # One liner version
    # return sum([n1 * (n1 == n2) for n1, n2 in zip(numbers, numbers[1:] + [numbers[0]])])

    # "classic" version
    tot = 0
    for n1, n2 in zip(numbers, numbers[1:] + [numbers[0]]):
        if n1 == n2:
            tot += n1
    return tot


def d1p2(input_text: str):
    numbers = list(map(int, input_text))
    half_length = len(numbers) // 2

    # One liner version
    return sum([n1 * (n1 == n2) for n1, n2 in zip(numbers, numbers[half_length:] + numbers[:half_length])])

    # "classic" version
    # tot = 0
    # for n1, n2 in zip(numbers, numbers[half_length:] + numbers[:half_length]):
    #     if n1 == n2:
    #         tot += n1
    # return tot


if __name__ == '__main__':
    day, year = 1, 2017
    txt = python_utils.get_input(day, year)
    print(f'Part 1: {d1p1(txt)}')
    print(f'Part 2: {d1p2(txt)}')
