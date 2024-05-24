import regex
from typing import List

import python_utils


def d1p1(lines: List[str]):
    line_digits = [regex.findall(r'\d', line) for line in lines]
    line_digits = [numbers[0] + numbers[-1] if len(numbers) > 1 else numbers[0] + numbers[0]
                   for numbers in line_digits]
    line_numbers = map(int, line_digits)
    return sum(line_numbers)


def d1p2(lines: List[str]):
    numbers_spelled = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7",
                       "eight": "8", "nine": "9"}
    reg = regex.compile('|'.join(numbers_spelled.keys()) + '|\d')
    numbers_spelled.update({str(n): str(n) for n in range(10)})

    line_digits = [regex.findall(reg, line, overlapped=True) for line in lines]
    line_digits = [numbers_spelled[digits[0]] + numbers_spelled[digits[-1]] if len(digits) > 1
                   else numbers_spelled[digits[0]] + numbers_spelled[digits[0]]
                   for digits in line_digits]
    line_numbers = map(int, line_digits)
    return sum(line_numbers)


if __name__ == '__main__':
    lines = python_utils.get_input_as_lines(1, 2023)
    print(f"Part 1: {d1p1(lines)}")
    print(f"Part 2: {d1p2(lines)}")
