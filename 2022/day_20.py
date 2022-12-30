from typing import Tuple, List

import python_utils


def mix_data(original: List[Tuple[int, int]], current: List[Tuple[int, int]]):
    for id, original_val in original:
        idx_val = current.index((id, original_val))
        # If val is bigger than list's length we don't count mod N, but mod N-1 as val is actually part of `current`
        val = original_val % (len(current) - 1)

        # list.insert(idx) puts the value BEFORE the index given, hence we add 1 for forward walk
        insert_idx = (idx_val + val + (1 if val > 0 else 0)) % len(current)

        # Backward walks never stops on 0, it "overflows" at the end of the list
        if val < 0 and insert_idx == 0:
            insert_idx = len(current)

        # Insert value in the new position
        current.insert(insert_idx, (id, original_val))

        # We now have (at least) 2 identical values in different positions, pop the right one, i.e.
        # i) not the position we just inserted and ii) the same ID we just processed
        current.pop(next(i for i, (id_pop, x) in enumerate(current)
                         if x == original_val and id_pop == id and i != insert_idx))

    return current


def output(values: List[Tuple[int, int]]):
    idx_zero = next(i for i, (_, v) in enumerate(values) if v == 0)
    v1 = values[(idx_zero + 1000) % len(values)][1]
    v2 = values[(idx_zero + 2000) % len(values)][1]
    v3 = values[(idx_zero + 3000) % len(values)][1]
    return v1 + v2 + v3


def d20p1(data: str):
    # NOTE: input data are NOT unique numbers (1 hour burned cause of this)
    # To solve above, store data as list of tuples: i) unique ID (enumeration) and ii) actual integer
    original = list(enumerate(python_utils.parse_ints(data)))
    values = original.copy()
    values = mix_data(original, values)
    return output(values)


def d20p2(data: str):
    # We can reuse everything, just see above for clues of the method
    # Just wait a bunch of seconds for computation :)
    integers = [x * 811589153 for x in python_utils.parse_ints(data)]
    original = list(enumerate(integers))
    values = original.copy()
    for _ in range(10):
        values = mix_data(original, values)

    return output(values)


if __name__ == '__main__':
    data = python_utils.get_input(20, 2022)
    print(f"Part 1: {d20p1(data)}")
    print(f"Part 2: {d20p2(data)}")
