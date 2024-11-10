import collections
import datetime
import re
from typing import List, Dict

import python_utils


def get_time_counts(lines: List[str]) -> Dict[int, collections.Counter]:
    lines = sorted(lines)
    times = {}

    curr_id = start_time = -1
    for line in lines:
        date_str = re.findall('\[(.+)\]', line)[0]
        line_time = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M")
        if "Guard" in line:
            curr_id = python_utils.parse_ints(line)[-1]
        elif "falls asleep" in line:
            start_time = line_time
        elif "wakes up" in line:
            times[curr_id].update(collections.Counter(range(start_time.minute, line_time.minute)))

    return times


def d4p1(lines: List[str]):
    # First solution that comes to mind is to count how many times for each minute a guard is sleeping
    times = get_time_counts(lines)
    max_id = max(times, key=lambda k: sum(times[k].values()))
    return max_id * times[max_id].most_common(1)[0][0]


def d4p2(lines: List[str]):
    # Just swap sum with max :)
    times = get_time_counts(lines)
    max_id = max(times, key=lambda k: max(times[k].values()))
    return max_id * times[max_id].most_common(1)[0][0]


if __name__ == '__main__':
    day, year = 4, 2018
    lines = python_utils.get_input_as_lines(day, year)
    print(f'Part 1: {d4p1(lines)}')
    print(f'Part 2: {d4p2(lines)}')
