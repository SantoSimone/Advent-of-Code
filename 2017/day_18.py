import collections
from typing import List, Dict

import python_utils


def d18p1(lines: List[str]):
    registers = collections.defaultdict(int)
    idx = 0
    last_sound = 0
    while idx < len(lines):
        curr_line = lines[idx]
        ins, *ops = curr_line.strip().split()
        op1 = ops[0] if ops[0].isalpha() else int(ops[0])
        if len(ops) == 2:
            op2 = registers[ops[1]] if ops[1].isalpha() else int(ops[1])
        if ins == 'snd':
            last_sound = registers[op1]
        elif ins == 'set':
            registers[op1] = op2
        elif ins == 'add':
            registers[op1] += op2
        elif ins == 'mul':
            registers[op1] *= op2
        elif ins == 'mod':
            registers[op1] = registers[op1] % op2
        elif ins == 'rcv' and op1:
            return last_sound
        elif 'jgz' in curr_line and registers[op1] > 0:
            idx += op2
            continue

        idx += 1

    return None


def process_program(state: Dict[str, int], queue_in: collections.deque, queue_out: collections.deque, lines: List[str]):
    # This function makes the program run up until the queue_in is empty or all instructions have been done

    while state['idx'] < len(lines):
        curr_line = lines[state['idx']]
        ins, *ops = curr_line.strip().split()
        op1 = ops[0] if ops[0].isalpha() else int(ops[0])
        if len(ops) == 2:
            op2 = state[ops[1]] if ops[1].isalpha() else int(ops[1])
        if ins == 'snd':
            queue_out.append(op1 if type(op1) == int else state[op1])
            state['sent'] += 1
        elif ins == 'set':
            state[op1] = op2
        elif ins == 'add':
            state[op1] += op2
        elif ins == 'mul':
            state[op1] *= op2
        elif ins == 'mod':
            state[op1] = state[op1] % op2
        elif ins == 'rcv':
            if len(queue_in) == 0:
                return
            state[op1] = queue_in.popleft()
        elif 'jgz' in curr_line:
            op1 = op1 if type(op1) == int else state[op1]
            if op1 > 0:
                state['idx'] += op2
                continue

        state['idx'] += 1


def d18p2(lines: List[str]):
    # Refactor part1 so that all variables are stored in "state" and add new behaviour of rcv and send
    # Then call the process until the deadlock is reached

    state_a = collections.defaultdict(int, {'p': 0})
    state_b = collections.defaultdict(int, {'p': 1})
    queue_a, queue_b = collections.deque([]), collections.deque([])
    while True:
        process_program(state_a, queue_a, queue_b, lines)
        process_program(state_b, queue_b, queue_a, lines)
        if len(queue_a) == 0 and len(queue_b) == 0:
            break

    return state_b['sent']


if __name__ == '__main__':
    day, year = 18, 2017
    lines = python_utils.get_input_as_lines(day, year)
    print(f'Part 1: {d18p1(lines)}')
    print(f'Part 2: {d18p2(lines)}')
