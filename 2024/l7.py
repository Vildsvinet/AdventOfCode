# Advent of Code, 2024, day 7

import sys

sys.setrecursionlimit(2 ** 12 + 1)

totsum = 0


def rollback(sofar):
    nodes, vals = [], []

    # first node never changes
    while len(sofar) > 1:
        value, multiply = sofar.pop()
        if not multiply: break
        vals.append(value)

    # the node that was previously plus is now mult
    nodes.append((value, True))

    # the rest restarts as plus
    for vs in vals:
        nodes.insert(1, (vs, False))

    return sofar + nodes


def run(sofar, result):
    global totsum

    # calculate equation
    res, _ = sofar[0]
    for e in sofar[1:]:
        val, mult = e
        res = (res * val if mult else res + val)

    # it was "correct":
    if res == result:
        totsum += result
        return True

    # we have exhausted all possibilities without success:
    elif all([node[1] for node in sofar[1:]]):
        return False

    # not correct, but keep looking (rollback):
    else:
        return run(rollback(sofar), result)


with open("i7.txt", 'r') as inp:
    for line in inp:
        # initial parsing
        numbers = line.strip().split(' ')
        numbers[0] = numbers[0].rstrip(':')
        numbers = list(map(int, numbers))

        # prepare the numbers with tuples, start with plus everywhere
        result = numbers.pop(0)
        first = [(numbers.pop(0), None)]  # no operator before first value
        rest = [(i, False) for i in numbers]

        run(first + rest, result)

    print(totsum)
