from typing import List

from python_utils import get_input_as_lines

opening = ['(', '[', '{', '<']
closing = [')', ']', '}', '>']


def d10p1(lines: List[str]):
    corrupt_score = 0
    scores = [3, 57, 1197, 25137]
    for line in lines:
        opened = []
        for c in line:
            if c in opening:
                opened.append(c)
            else:
                if c != closing[opening.index(opened[-1])]:
                    corrupt_score += scores[closing.index(c)]
                opened.pop(-1)
    return corrupt_score


def d10p2(lines: List[str]):
    incomplete_scores = []
    scores = [1, 2, 3, 4]
    for i, line in enumerate(lines):
        incomplete = True
        opened = []
        for c in line:
            if c in opening:
                opened.append(c)
            else:
                if c != closing[opening.index(opened[-1])]:
                    incomplete = False
                    break
                opened.pop(-1)

        if incomplete:
            incomplete_score = 0
            for c in opened[::-1]:
                incomplete_score *= 5
                incomplete_score += scores[opening.index(c)]
            incomplete_scores.append(incomplete_score)

    return sorted(incomplete_scores)[len(incomplete_scores) // 2]


if __name__ == '__main__':
    lines = get_input_as_lines(10, 2021)
    #     lines = """[({(<(())[]>[[{[]{<()<>>
    # [(()[<>])]({[<{<<[]>>(
    # {([(<{}[<>[]}>{[]{[(<()>
    # (((({<>}<{<{<>}{[]{[]{}
    # [[<[([]))<([[{}[[()]]]
    # [{[{({}]{}}([{[{{{}}([]
    # {<[[]]>}<{[{[{[]{()[[[]
    # [<(<(<(<{}))><([]([]()
    # <{([([[(<>()){}]>(<<{{
    # <{([{{}}[<[[[<>{}]]]>[]]""".splitlines()
    print(f"Part 1: {d10p1(lines)}")
    print(f"Part 2: {d10p2(lines)}")
