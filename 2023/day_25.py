import re
from typing import List

import networkx

import python_utils


def parse_components(lines: List[str]):
    graph = networkx.Graph()
    for line in lines:
        node, *neighbours = re.findall('\w+', line)
        graph.add_node(node)
        graph.add_edges_from([(node, neigh) for neigh in neighbours])

    return graph


def d25p1(lines: List[str]):
    # Networkx does everything for us, and I'm not in the mood for complex algorithm re-implementation :)
    graph = parse_components(lines)
    to_remove = networkx.minimum_edge_cut(graph)
    for edge in to_remove:
        graph.remove_edge(*edge)

    cc = networkx.connected_components(graph)
    return python_utils.multiply(map(len, cc))


if __name__ == '__main__':
    day, year = 25, 2023
    lines = python_utils.get_input_as_lines(day, year)
    print(f'Part 1: {d25p1(lines)}')
