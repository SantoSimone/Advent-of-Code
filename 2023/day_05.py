import re
import time
from typing import List, Tuple

import more_itertools

import python_utils


def parse_ranges(lines: List[str]) -> List[Tuple[int, int, int]]:
    all_ranges = []
    groups = python_utils.splitter(lines[2:], '')

    for group in groups:
        group_ranges = []
        for range_line in group[1:]:
            group_ranges.append(tuple(map(int, re.findall(r'\d+', range_line))))
        all_ranges.append(group_ranges)

    return all_ranges


def d5p1(lines: List[str]):
    seeds = map(int, re.findall(r'\d+', lines[0]))
    grouped_ranges = parse_ranges(lines)

    locations = []
    for seed in seeds:
        for group in grouped_ranges:
            for dst_start, src_start, length in group:
                if src_start <= seed < src_start + length:
                    seed = dst_start + (seed - src_start)
                    break

        locations.append(seed)

    return min(locations)


def d5p2(lines: List[str]):
    seeds = map(int, re.findall(r'\d+', lines[0]))
    grouped_ranges = parse_ranges(lines)

    locations = []
    for seed_start, seed_length in more_itertools.chunked(seeds, 2):
        for seed in range(seed_start, seed_start + seed_length):
            for group in grouped_ranges:
                for dst_start, src_start, length in group:
                    if src_start <= seed < src_start + length:
                        seed = dst_start + (seed - src_start)
                        break

            locations.append(seed)

    return min(locations)


if __name__ == '__main__':
    day, year = 5, 2023
    lines = python_utils.get_input_as_lines(day, year)
    #     lines = """seeds: 79 14 55 13
    #
    # seed-to-soil map:
    # 50 98 2
    # 52 50 48
    #
    # soil-to-fertilizer map:
    # 0 15 37
    # 37 52 2
    # 39 0 15
    #
    # fertilizer-to-water map:
    # 49 53 8
    # 0 11 42
    # 42 0 7
    # 57 7 4
    #
    # water-to-light map:
    # 88 18 7
    # 18 25 70
    #
    # light-to-temperature map:
    # 45 77 23
    # 81 45 19
    # 68 64 13
    #
    # temperature-to-humidity map:
    # 0 69 1
    # 1 0 69
    #
    # humidity-to-location map:
    # 60 56 37
    # 56 93 4""".splitlines()
    print(f'Part 1: {d5p1(lines)}')
    start = time.perf_counter()
    print(f'Part 2: {d5p2(lines)}')
    print(f"Total time: {time.perf_counter() - start}")
