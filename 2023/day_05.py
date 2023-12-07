import re
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
    seeds = python_utils.parse_ints(lines[0])
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
    # Code is a bit convoluted, but the idea is to perform mapping each seed chunk at a time instead of single seed
    # Btw, brute force took 2h 15min... this solution 5 ms :)
    seeds = python_utils.parse_ints(lines[0])
    grouped_ranges = parse_ranges(lines)

    chunk_to_check = [(start, start + length) for start, length in more_itertools.chunked(seeds, 2)]
    for group in grouped_ranges:
        new_chunks = []
        while chunk_to_check:
            curr_start, curr_end = chunk_to_check.pop()
            matched = []
            for dst_start, src_start, length in group:
                intersection_start = max(curr_start, src_start)
                intersection_end = min(curr_end, src_start + length)
                if intersection_start < intersection_end - 1:
                    new_chunks.append(
                        (dst_start + (intersection_start - src_start),
                         dst_start + (intersection_start - src_start) + (intersection_end - intersection_start))
                    )
                    matched.append((intersection_start, intersection_end))
            else:
                # Check that the current chunk has been fully covered
                fill_start = curr_start
                matched = sorted(matched)
                for start, end in matched:
                    if start > fill_start:
                        new_chunks.append((fill_start, start))
                    fill_start = end + 1
                else:
                    if curr_end > fill_start:
                        new_chunks.append((fill_start, curr_end))

        chunk_to_check = new_chunks

    return min(chunk_min for chunk_min, _ in chunk_to_check)


if __name__ == '__main__':
    day, year = 5, 2023
    lines = python_utils.get_input_as_lines(day, year)
    print(f'Part 1: {d5p1(lines)}')
    print(f'Part 2: {d5p2(lines)}')
