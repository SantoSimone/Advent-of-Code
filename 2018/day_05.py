import python_utils


def react(text: str) -> str:
    changed = True
    while changed:
        changed = False
        to_remove = set()
        i = 0
        while i < len(text) - 1:
            c1, c2 = text[i:i + 2]
            if (
                    (c1.islower() and c2 == c1.upper()) or
                    (c1.isupper() and c2 == c1.lower())
            ):
                to_remove.add(i)
                to_remove.add(i + 1)
                changed = True
                i += 1

            i += 1

        text = ''.join([c for i, c in enumerate(text) if i not in to_remove])

    return text


def d5p1(input_text: str):
    # Brute force, it doesn't take long (10-ish seconds)

    return len(react(input_text))


def d5p2(input_text: str):
    # Optimize by solving first part and start searching from there

    first_part = react(input_text)
    possible_removes = set(first_part.lower())

    return min(len(react(first_part.replace(p.lower(), '').replace(p.upper(), '')))
               for p in possible_removes)


if __name__ == '__main__':
    day, year = 5, 2018
    txt = python_utils.get_input(day, year)
    print(f'Part 1: {d5p1(txt)}')
    print(f'Part 2: {d5p2(txt)}')
