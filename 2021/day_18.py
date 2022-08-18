import itertools
import math
import re
from typing import List, Union, Tuple

import numpy as np

from python_utils import get_input_as_lines


class Pair:
    def __init__(self, lhs: "Pair" = None, rhs: "Pair" = None):
        self.lhs: Union[int, Pair] = lhs
        self.rhs: Union[int, Pair] = rhs

    def explode(self) -> Tuple[bool, str]:
        text = self.to_string()
        depth = 0
        pos = 0
        exploded = False
        while pos < len(text):
            if depth > 4:
                pos -= 1
                if text[pos] != '[':
                    pos += 2
                end_pos = text.find(']', pos)
                lhs, rhs = re.findall(r'\d+', text[pos:end_pos + 1])
                start_lhs = pos + 1
                end_lhs = start_lhs + len(lhs)
                start_rhs = end_lhs + 1
                end_rhs = start_rhs + len(rhs)

                regex = re.findall(r'\d+', text[:pos])
                if len(regex) > 0:
                    replace_left_pos = text[:start_lhs].rfind(regex[-1])
                    left_part = text[:replace_left_pos] + str(int(text[start_lhs:end_lhs]) + int(regex[-1])) + \
                                text[replace_left_pos + (1 if len(regex[-1]) == 1 else 2):pos]
                else:
                    left_part = text[:pos]

                regex = re.findall(r'\d+', text[pos + 6:])
                if len(regex) > 0:
                    replace_right_pos = text.find(regex[0], end_pos)
                    right_part = text[end_pos + 1:replace_right_pos] + \
                                 str(int(text[start_rhs:end_rhs]) + int(regex[0])) + \
                                 text[replace_right_pos + (1 if len(regex[0]) == 1 else 2):]
                else:
                    right_part = text[end_pos:]

                text = f"{left_part}0{right_part}"
                exploded = True

                break

            elif text[pos] == '[':
                depth += 1
            elif text[pos] == ']':
                depth -= 1

            pos += 1

        return exploded, text

    def split(self) -> bool:
        if type(self.lhs) == int and self.lhs > 9:
            p = Pair()
            p.lhs = self.lhs // 2
            p.rhs = self.lhs - self.lhs // 2
            self.lhs = p
            return True
        elif type(self.lhs) == Pair:
            if self.lhs.split():
                return True

        if type(self.rhs) == int and self.rhs > 9:
            p = Pair()
            p.lhs = self.rhs // 2
            p.rhs = self.rhs - self.rhs // 2
            self.rhs = p
            return True
        elif type(self.rhs) == Pair:
            return self.rhs.split()

        return False

    def reduce(self):
        exploded = True
        split = True
        while exploded or split:
            exploded, new_text = self.explode()
            if exploded:
                p, _ = parse_pair(new_text, 0)
                self.lhs = p.lhs
                self.rhs = p.rhs
                continue

            split = self.split()

        return self

    def to_string(self):
        lhs_str = f"{self.lhs}" if type(self.lhs) == int else self.lhs.to_string()
        rhs_str = f"{self.rhs}" if type(self.rhs) == int else self.rhs.to_string()
        return f"[{lhs_str},{rhs_str}]"

    def magnitude(self):
        lhs_mag = 3 * (self.lhs if type(self.lhs) == int else self.lhs.magnitude())
        rhs_mag = 2 * (self.rhs if type(self.rhs) == int else self.rhs.magnitude())

        return lhs_mag + rhs_mag


def parse_pair(line: str, pos: int) -> Tuple[Pair, int]:
    assert line[pos] == '['
    pos += 1
    p = Pair()
    parsing_lhs = True
    while True:
        if line[pos] == '[':
            pp, pos = parse_pair(line, pos)
            if parsing_lhs:
                p.lhs = pp
            else:
                p.rhs = pp

        elif line[pos] == ',':
            parsing_lhs = False

        elif line[pos] == ']':
            break

        else:  # its a number
            if '0' <= line[pos + 1] <= '9':
                v = int(line[pos:pos + 2])
                pos += 1
            else:
                v = int(line[pos])
            if parsing_lhs:
                p.lhs = v
            else:
                p.rhs = v

        pos += 1

    return p, pos


def d18p1(lines: List[str]):
    p = parse_pair(lines[0], 0)[0]
    for line in lines[1:]:
        p = Pair(p, parse_pair(line, 0)[0])
        p.reduce()

    return p.magnitude()


def d18p2(lines: List[str]):
    # Today's code is crappy but I want to completely ruin it now (plus slow runtime)
    return max(
        [Pair(parse_pair(l1, 0)[0], parse_pair(l2, 0)[0]).reduce().magnitude()
         for l1, l2 in itertools.permutations(lines, 2)]
    )


if __name__ == '__main__':
    lines = get_input_as_lines(18, 2021)
    print(f"Part 1: {d18p1(lines)}")
    print(f"Part 2: {d18p2(lines)}")
