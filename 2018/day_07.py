import collections
import re
from typing import List, Dict, Set, Tuple

import python_utils


def parse_lines(lines) -> Tuple[Set[str], Dict[str, List[str]]]:
    requires = collections.defaultdict(list)
    all_steps = set()
    for line in lines:
        first, second = re.findall('step (\w)', line.lower())
        requires[second].append(first)
        all_steps.add(first)
        all_steps.add(second)
    return all_steps, requires


def d7p1(lines: List[str]):
    all_steps, requires = parse_lines(lines)

    all_steps = sorted(all_steps)
    done = []
    while len(all_steps) > 0:
        for s in all_steps:
            if len(requires[s]) == 0:
                all_steps.remove(s)
                done.append(s)

                for k in requires.keys():
                    if s in requires[k]:
                        requires[k].pop(requires[k].index(s))

                break

    return ''.join(done).upper()


def d7p2(lines: List[str]):
    all_steps, requires = parse_lines(lines)

    all_steps = sorted(all_steps)
    done = []
    workers = {}
    total = 0
    while len(done) != len(all_steps) or len(workers) > 0:
        working = [s for s, _ in workers.values()]
        for s in all_steps:
            if s in done or s in working:
                continue

            if len(requires[s]) == 0 and len(workers) < 5:
                workers[set(range(5)).difference(set(workers.keys())).pop()] = (s, ord(s) - ord('a') + 61)

        finished_workers = []
        for worker in workers.keys():
            step, remaining = workers[worker]
            workers[worker] = (step, remaining - 1)
            if remaining - 1 == 0:
                done.append(step)
                finished_workers.append(worker)

                for k in requires.keys():
                    if step in requires[k]:
                        requires[k].pop(requires[k].index(step))

        for worker in finished_workers:
            workers.pop(worker)

        total += 1

    return total


if __name__ == '__main__':
    day, year = 7, 2018
    lines = python_utils.get_input_as_lines(day, year)
    #     lines = """Step C must be finished before step A can begin.
    # Step C must be finished before step F can begin.
    # Step A must be finished before step B can begin.
    # Step A must be finished before step D can begin.
    # Step B must be finished before step E can begin.
    # Step D must be finished before step E can begin.
    # Step F must be finished before step E can begin.""".splitlines()
    print(f'Part 1: {d7p1(lines)}')
    print(f'Part 2: {d7p2(lines)}')
