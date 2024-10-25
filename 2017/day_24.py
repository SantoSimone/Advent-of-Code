import collections
from typing import List, Dict

import python_utils


def get_components(lines: List[str]) -> Dict[int, List[int]]:
    # Describe components as "which pin can be connected to which pin"
    components = collections.defaultdict(list)
    for line in lines:
        c1, c2 = python_utils.parse_ints(line)

        components[c1].append(c2)
        components[c2].append(c1)

    return components


def get_all_builds(components: Dict[int, List[int]]) -> List[List[List[int]]]:
    all_builds = []
    q = [[[0, 0]]]
    while q:
        curr_bridge = q.pop()
        curr = curr_bridge[-1]
        all_builds.append(curr_bridge)

        for next_pin in components[curr[1]]:
            # Check that we didn't use the (next_pin, curr_pin) component yet
            if [next_pin, curr[1]] in curr_bridge or [curr[1], next_pin] in curr_bridge:
                continue

            q.append([*curr_bridge, [curr[1], next_pin]])

    return all_builds


def d24p1(lines: List[str]):
    # This is a regular Depth First Search

    components = get_components(lines)
    all_builds = get_all_builds(components)
    strenghts = [sum([sum(b) for b in build]) for build in all_builds]
    return max(strenghts)


def d24p2(lines: List[str]):
    # Re-use part 1 and add some computation

    components = get_components(lines)
    all_builds = get_all_builds(components)
    max_length = max(map(len, all_builds))
    all_builds = filter(lambda b: len(b) == max_length, all_builds)
    strenghts = map(lambda build: sum([sum(b) for b in build]), all_builds)
    return max(strenghts)


if __name__ == '__main__':
    day, year = 24, 2017
    lines = python_utils.get_input_as_lines(day, year)
    print(f'Part 1: {d24p1(lines)}')
    print(f'Part 2: {d24p2(lines)}')
