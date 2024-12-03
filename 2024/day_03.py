import re

import python_utils


def d3p1(input_txt: str):
    valid_muls = re.findall('mul\((\d+),(\d+)\)', input_txt)
    valid_muls = [map(int, mul) for mul in valid_muls]
    mul_values = map(python_utils.multiply, valid_muls)

    return sum(mul_values)


def d3p2(input_txt: str):
    all_instructions = re.finditer(
        "mul\((\d+),(\d+)\)|do\(\)|don't\(\)",
        input_txt
    )
    should_add = True
    tot = 0
    for ins in all_instructions:
        span = input_txt[ins.start():ins.end()]
        if "don't" in span:
            should_add = False
        elif "do" in span:
            should_add = True
        if 'mul' in span and should_add:
            tot += python_utils.multiply(map(int, ins.groups()))

    return tot


if __name__ == '__main__':
    day, year = 3, 2024
    lines = python_utils.get_input(day, year)
    print(f'Part 1: {d3p1(lines)}')
    print(f'Part 2: {d3p2(lines)}')
