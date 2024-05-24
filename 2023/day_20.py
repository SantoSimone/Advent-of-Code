import collections
import re
from typing import List, Tuple, Dict

import python_utils


def parse_input(lines: List[str]):
    mapping = {}
    flipflops, conjunctions = [], []
    for line in lines:
        name, *outputs = re.findall(r'\w+', line)
        mapping[name] = outputs

        if line.startswith('%'):
            flipflops.append(name)
        elif line.startswith('&'):
            conjunctions.append(name)

    return mapping, flipflops, conjunctions


def compute_effects(graph: Dict[str, List[str]], ff_states: Dict[str, bool], conj_states: Dict[str, Dict[str, bool]],
                    flipflops: List[str], conjunctions: List[str],
                    src: str, pulse: bool, dst: str) -> List[Tuple[str, bool, str]]:
    if dst == 'broadcaster':
        return [('broadcaster', pulse, out) for out in graph['broadcaster']]

    elif not pulse and dst in flipflops:
        ff_states[dst] = not ff_states[dst]
        return [(dst, ff_states[dst], out) for out in graph[dst]]

    elif dst in conjunctions:
        conj_states[dst][src] = pulse
        next_pulse = False if all(x for x in conj_states[dst].values()) else True
        return [(dst, next_pulse, out) for out in graph[dst]]

    return []


def d20p1(lines: List[str]):
    # We use the convention: False -> low pulse / True -> high pulse
    mapping, flipflops, conjunctions = parse_input(lines)
    flipflops_state = {name: False for name in flipflops}
    conjunction_state = collections.defaultdict(dict)

    for inp, outs in mapping.items():
        for conj in filter(lambda x: x in conjunctions, outs):
            conjunction_state[conj][inp] = False

    high_pulses = low_pulses = 0
    for _ in range(1000):
        pulses = collections.deque([('button', False, 'broadcaster')])
        while pulses:
            src, pulse, dst = pulses.popleft()
            high_pulses += pulse
            low_pulses += not pulse
            next_round = compute_effects(mapping, flipflops_state, conjunction_state, flipflops, conjunctions,
                                         src, pulse, dst)
            pulses.extend(next_round)

    return high_pulses * low_pulses


def find_periods(graph: Dict[str, List[str]], ff_states: Dict[str, bool], conj_states: Dict[str, Dict[str, bool]],
                 flipflops: List[str], conjunctions: List[str]):
    # NOTE: 'rx' is activated by 'X' and all nodes containing 'X' are conjunctions that need to receive a high pulse
    # in order to activate 'X' which in turn will send low pulse to 'rx'
    periodic = set()
    rx_source = None

    for src, outs in graph.items():
        if outs == ['rx']:
            rx_source = src
            break

    for src, outs in graph.items():
        if rx_source in outs:
            periodic.add(src)

    i = 0
    periods = {}
    while True:
        pulses = collections.deque([('button', False, 'broadcaster')])
        i += 1

        if not periodic:
            break

        while pulses:
            src, pulse, dst = pulses.popleft()

            if not pulse:
                if dst in periodic:
                    periods[dst] = i
                    periodic.discard(dst)

            next_round = compute_effects(graph, ff_states, conj_states, flipflops, conjunctions, src, pulse, dst)
            pulses.extend(next_round)

    return periods


def d20p2(lines: List[str]):
    # Seems like we need to hack the input on this day.. won't strive for good code
    mapping, flipflops, conjunctions = parse_input(lines)
    flipflops_state = {name: False for name in flipflops}
    conjunction_state = collections.defaultdict(dict)

    for inp, outs in mapping.items():
        for conj in filter(lambda x: x in conjunctions, outs):
            conjunction_state[conj][inp] = False

    periods = find_periods(mapping, flipflops_state, conjunction_state, flipflops, conjunctions)

    return python_utils.multiply(periods.values())


if __name__ == '__main__':
    day, year = 20, 2023
    lines = python_utils.get_input_as_lines(day, year)
    #     lines = """broadcaster -> a
    # %a -> inv, con
    # &inv -> b
    # %b -> con
    # &con -> output""".splitlines()
    print(f'Part 1: {d20p1(lines)}')
    print(f'Part 2: {d20p2(lines)}')
