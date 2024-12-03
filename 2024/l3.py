# Advent of Code, 2024, day 3
import re


def p1(st: str) -> int:
    st_sum = 0
    muls = re.findall('mul\([0-9][0-9]?[0-9]?,[0-9][0-9]?[0-9]?\)', st)
    for mul in muls:
        _, a, b, _ = re.split('[(,)]', mul)
        st_sum += int(a) * int(b)
    return st_sum


with open("i3.txt", 'r') as inp:
    totsum = 0
    for l in inp:
        totsum += p1(l)
    print(totsum)
