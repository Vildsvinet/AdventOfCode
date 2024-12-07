# Advent of Code, 2024, day 7


# importing the sys module
import sys

# the setrecursionlimit function is
# used to modify the default recursion
# limit set by python. Using this,
# we can increase the recursion limit
# to satisfy our needs

sys.setrecursionlimit(10 ** 6)

totsum = 0
antalrotationer = 0

def rollback(sofar):
    nodes = []
    vals = []
    while sofar :
        value, multiply = sofar.pop()
        if multiply: vals.append(value)
        else:
            nodes.append((value, True))
            for vs in vals:
                nodes.insert(1, (vs, False))
            break
    return sofar, nodes


def run(sofar, nrs, result):
    # print(result, first, rest)
    global totsum, antalrotationer
    if not nrs:     # nrs empty, we are at a leaf
        # if not sofar: return False
        # [print(f"\t {i} \t ", end='') for i in sofar]
        # print("")
        antalrotationer += 1
        res, _ = sofar[0]
        for e in sofar[1:]:
            val, mult = e
            res = (res * val if mult else res + val)
        if res == result:
            totsum += result
            # [print(f"\t {i} \t ", end='') for i in sofar]
            # print("")
            return True
        elif all([test[1] for test in sofar]):
            return False
        else:
            sofar, nrs = rollback(sofar)
            return run(sofar, nrs, result)
    else:
        sofar.append(nrs.pop(0))
        return run(sofar, nrs, result)


with open("i7.txt", 'r') as inp:
    for line in inp:
        numbers = line.strip().split(' ')
        numbers[0] = numbers[0].rstrip(':')
        numbers = list(map(int, numbers))
        # print(numbers)

        result = numbers.pop(0)
        first = [(numbers.pop(0), False)]
        rest = [(i, False) for i in numbers]

        # print(result, first, rest)
        #
        run(first, rest, result)
    #
    print(totsum)
    print(antalrotationer)


