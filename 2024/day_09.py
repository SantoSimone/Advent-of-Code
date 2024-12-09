import bisect
import collections

import python_utils


def d9p1(input_text: str):
    # Construct all blocks while keeping track of where we left free spaces

    amphipods = []
    curr_id = 0
    is_file = True
    free_space = collections.deque([])
    curr_idx = 0
    for num in map(int, input_text):
        if is_file:
            amphipods.extend([curr_id] * num)
            curr_id += 1
        else:
            amphipods.extend([None] * num)
            free_space.extend(range(curr_idx, len(amphipods)))

        curr_idx = len(amphipods)
        is_file = not is_file

    # Re-arrangement
    while free_space:
        rightmost = amphipods.pop()
        if rightmost is None:
            free_space.pop()
            continue

        leftmost_free = free_space.popleft()
        amphipods[leftmost_free] = rightmost

    # Some "pythonic" unreadable code
    return sum(map(python_utils.multiply, zip(amphipods, range(len(amphipods)))))


def d9p2(input_text: str):
    # Same idea, but we need to change data structures: now we keep track of free spaces as a dictionary of
    # size -> list of possible locations; we also keep track of file size and index in a dictionary, so we avoid
    # filling a huge list
    # Moreover, we try a new fancy way of parsing input

    input_nums = list(map(int, input_text))
    indices = [0] + list(python_utils.cumsum(input_nums))
    files = {file_id: (idx, size) for file_id, idx, size in zip(range(len(input_nums)), indices[::2], input_nums[::2])}
    free_space = collections.defaultdict(collections.deque)
    for size, idx in zip(input_nums[1::2], indices[1::2]):
        free_space[size].append(idx)

    for curr_file in reversed(range(max(files) + 1)):
        file_idx, file_size = files[curr_file]
        candidate_sizes = [(size, indices)
                           for size, indices in free_space.items()
                           if size >= file_size and len(indices) > 0]
        candidate_sizes = sorted(candidate_sizes, key=lambda candidate: min(candidate[1]))

        if candidate_sizes:
            free_space_size, _ = candidate_sizes[0]
            leftmost_free_space_idx = free_space[free_space_size].popleft()
            if leftmost_free_space_idx > file_idx:
                continue

            # If the search size is bigger than the current size, we update the free_space dict
            if free_space_size - file_size > 0:
                bisect.insort(free_space[free_space_size - file_size], leftmost_free_space_idx + file_size)

            files[curr_file] = (leftmost_free_space_idx, file_size)

    checksum = sum([
        file_id * (file_idx + i)
        for file_id, (file_idx, file_size) in files.items()
        for i in range(file_size)
    ])

    return checksum


if __name__ == '__main__':
    day, year = 9, 2024
    txt = python_utils.get_input(day, year)
    print(f'Part 1: {d9p1(txt)}')
    print(f'Part 2: {d9p2(txt)}')
