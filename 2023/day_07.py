import collections
import functools
from typing import List

import python_utils

# Defined it low-to-high so that using `find` will give the higher ranking with the `<` operator
CARD_VALUES = "23456789TJQKA"


def sub_jokers(counter: collections.Counter):
    if 'J' in counter:
        num_jokers = counter['J']
        del counter['J']
        if counter:
            # Find the highest card with highest frequency, i.e. sort by frequency AND index of card values
            most_common_card_with_bid = sorted(counter.most_common(),
                                               key=lambda x: (x[1], CARD_VALUES.find(x[0])), reverse=True)[0]
            most_common_card = most_common_card_with_bid[0]
            counter[most_common_card] += num_jokers
        else:
            counter['A'] = num_jokers


def compare(card_with_bid1: List[str], card_with_bid2: List[str], substitute_jokers: bool = False) -> int:
    lhs, rhs = card_with_bid1[0], card_with_bid2[0]
    lhs_counter = collections.Counter(lhs)
    rhs_counter = collections.Counter(rhs)

    if substitute_jokers:
        sub_jokers(lhs_counter)
        sub_jokers(rhs_counter)

    lhs_values = sorted(lhs_counter.values(), reverse=True)
    rhs_values = sorted(rhs_counter.values(), reverse=True)

    if lhs_values < rhs_values:
        return -1
    elif lhs_values > rhs_values:
        return 1

    # Break tie
    for i, c in enumerate(lhs):
        if c == rhs[i]:
            continue

        return -1 if CARD_VALUES.find(c) < CARD_VALUES.find(rhs[i]) else 1

    return 0


def d7p1(lines: List[str]):
    # Just sort by highest frequencies
    cards_with_bids = [line.split(' ') for line in lines]
    cards_with_bids = sorted(cards_with_bids, key=functools.cmp_to_key(compare))
    return sum(rank * int(bid) for rank, (_, bid) in enumerate(cards_with_bids, start=1))


def d7p2(lines: List[str]):
    # First change the values of cards, then swap jokers with most frequent (and highest card if tie occurs)
    global CARD_VALUES
    CARD_VALUES = "J23456789TQKA"

    cards_with_bids = [line.split(' ') for line in lines]
    cmp_func = functools.partial(compare, substitute_jokers=True)
    cards_with_bids = sorted(cards_with_bids, key=functools.cmp_to_key(cmp_func))
    return sum(rank * int(bid) for rank, (_, bid) in enumerate(cards_with_bids, start=1))


if __name__ == '__main__':
    day, year = 7, 2023
    lines = python_utils.get_input_as_lines(day, year)
    print(f'Part 1: {d7p1(lines)}')
    print(f'Part 2: {d7p2(lines)}')
