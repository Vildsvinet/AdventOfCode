# Advent of Code, 2024, day 7

import sys

sys.setrecursionlimit(3 ** 12 + 1)

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




################################## PART 2 ######################################

def concat(a, b): return int(str(a) + str(b))
def plus(a, b): return a + b
def times(a, b): return a * b


class Node:
    def __init__(self, value, operator):
        self.value = value
        self.operator = operator

    def next_operator(self):
        if self.operator == concat:
            self.operator = plus
        elif self.operator == plus:
            self.operator = times
        elif self.operator == times:
            self.operator = None

    def reset_operator(self):
        self.operator = concat

    def __str__(self):
        return f"{self.operator} : {self.value}"


# only for calculating a specific combination
def calculate_list(ls):
    l = ls[:]
    if len(l) == 2:
        return l[1].operator(l[0].value, l[1].value)
    nod0 = l.pop(0)
    nod1 = l.pop(0)
    new = Node(nod1.operator(nod0.value, nod1.value), None)
    return calculate_list([new] + l)


# move to the next (right) branch of the tree
def rollback_list(ls: list[Node]) -> list:
    l = ls[:]
    keep = [l.pop(0)]

    for pos, n in reversed(list(enumerate(l))):
        if n.operator != times:
            n.next_operator()
            for m in l[pos + 1:]:
                m.reset_operator()
            return keep + l
    return None


# pre: lista is Node objects, full length... quite pointless to do recursion
def run_recursive(lista, res):
    if not lista:  # we went to everything and found nothing
        return False
    if calculate_list(lista) == res:  # we found a match for the operators
        return True

    return run_recursive(rollback_list(lista), res)


def run_loop(lista, res):
    while True:
        if not lista:  # we went to everything and found nothing
            return False
        if calculate_list(lista) == res:  # we found a match for the operators
            return True
        lista = rollback_list(lista)


# pre: one line of the input
def part2(values: list, res: int) -> bool:
    nodes = [Node(values.pop(0), None)]
    while values:
        nodes.append(Node(values.pop(0), concat))

    return run_recursive(nodes, res)


with open("i7.txt", 'r') as inp:
    part2sum = 0
    for line in inp:
        # initial parsing
        numbers = line.strip().split(' ')
        numbers[0] = numbers[0].rstrip(':')
        numbers = list(map(int, numbers))

        # prepare the numbers with tuples, start with plus everywhere
        result = numbers.pop(0)
        # first = [(numbers.pop(0), None)]  # no operator before first value
        # rest = [(i, False) for i in numbers]

        # run(first + rest, result)

        if part2(numbers, result): part2sum += result

    # print(totsum)
    print(part2sum)
