import math
import re
from typing import List, Tuple, Dict

import python_utils


def parse_input(lines: List[str]) -> Tuple[str, Dict[str, Tuple[str, str]]]:
    instructions = lines[0]
    nodes = {}
    for line in lines[2:]:
        node, left, right = re.findall(r'\w+', line)
        nodes[node] = (left, right)

    return instructions, nodes


def d8p1(lines: List[str]):
    instructions, nodes = parse_input(lines)
    num_instructions = len(instructions)

    curr_node = "AAA"
    steps = 0
    while curr_node != "ZZZ":
        idx = (steps % num_instructions)
        curr_node = nodes[curr_node][0] if instructions[idx] == "L" else nodes[curr_node][1]
        steps += 1

    return steps


def find_loop(start_node: str, nodes: Dict[str, Tuple[str, str]], instructions: str):
    # Find the length of loop for each node, assuming they have one (and they obviously have, AoC expert here)
    # We assume that there's only one end node for each start node, i.e. `visits` will have only 1 key
    # We also assume that all nodes find their end node at the same idx (for my input was 306)
    # We assume all of this because the general solution is definitely hard to be implemented and I guess we are too
    # early in this year's calendar to have such hard problems :)

    visits = {}
    num_instructions = len(instructions)
    steps = 0
    while True:
        idx = (steps % num_instructions)
        start_node = nodes[start_node][0] if instructions[idx] == "L" else nodes[start_node][1]
        if start_node.endswith("Z"):
            if (idx, start_node) in visits:
                return steps - visits[idx, start_node]
            visits[idx, start_node] = steps
        steps += 1


def d8p2(lines: List[str]):
    # Everything is explained in the `find_loop` function
    instructions, nodes = parse_input(lines)
    loops = [find_loop(node, nodes, instructions) for node in nodes.keys()]
    return math.lcm(*loops)


if __name__ == '__main__':
    day, year = 8, 2023
    lines = python_utils.get_input_as_lines(day, year)
    print(f'Part 1: {d8p1(lines)}')
    print(f'Part 2: {d8p2(lines)}')
