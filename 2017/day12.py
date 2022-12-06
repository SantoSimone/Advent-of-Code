import itertools
import re
from typing import List

import networkx

import python_utils


def d12(lines: List[str]):
    # Networkx is so powerful
    graph = networkx.Graph()
    for line in lines:
        nodes = re.findall(r'\d+', line)
        graph.add_nodes_from(nodes)
        graph.add_edges_from(itertools.product(nodes[0:1], nodes[1:]))

    return len(networkx.node_connected_component(graph, '0')), networkx.number_connected_components(graph)


if __name__ == '__main__':
    lines = python_utils.get_input_as_lines(12, 2017)
    print(d12(lines))
