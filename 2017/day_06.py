import python_utils


def d6p1(input_text: str):
    config = python_utils.parse_ints(input_text)

    seen = {tuple(config)}
    num_banks = len(config)
    steps = 0
    while True:
        highest_idx = max(range(num_banks), key=lambda i: config[i])
        rounds = config[highest_idx]
        config[highest_idx] = 0
        for di in range(rounds):
            config[(highest_idx + 1 + di) % num_banks] += 1

        steps += 1
        if tuple(config) in seen:
            break

        seen.add(tuple(config))

    return steps


def d6p2(input_text: str):
    config = python_utils.parse_ints(input_text)

    seen = {tuple(config)}
    num_banks = len(config)
    steps = 0
    target = None
    first_appearance = -1
    while True:
        highest_idx = max(range(num_banks), key=lambda i: config[i])
        rounds = config[highest_idx]
        config[highest_idx] = 0
        for di in range(rounds):
            config[(highest_idx + 1 + di) % num_banks] += 1

        steps += 1
        if tuple(config) == target:
            break
        if tuple(config) in seen and target is None:
            target = tuple(config)
            first_appearance = steps

        seen.add(tuple(config))

    return steps - first_appearance


if __name__ == '__main__':
    day, year = 6, 2017
    txt = python_utils.get_input(day, year)
    print(f'Part 1: {d6p1(txt)}')
    print(f'Part 2: {d6p2(txt)}')
