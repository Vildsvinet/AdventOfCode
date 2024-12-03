# Advent of Code, 2024, day 3
import re


# use regexp to find valid muls and calculate them to return their sum
def p1(st: str) -> int:
    st_sum = 0
    muls = re.findall('mul\([0-9][0-9]?[0-9]?,[0-9][0-9]?[0-9]?\)', st)
    for mul in muls:
        _, a, b, _ = re.split('[(,)]', mul)
        st_sum += int(a) * int(b)
    return st_sum


# preprocess the data to return a list with only those chunks to be included
def pre(full: str) -> list[str]:
    todo_list = []
    dont_split = re.split("don't\(\)", full)
    todo_list.append(dont_split[0])  # first one always included

    for el in dont_split[1:]:
        do_split = re.split('do\(\)', el)

        if len(do_split) == 1:  # no Do()'s in this chunk
            continue
        else:
            todo_list += do_split[1:]  # everything from first Do() and onwards
    return todo_list


# preprocess then loop and apply solution from p1
def p2(txt: str) -> int:
    totsum = 0
    chunks : list[str] = pre(txt)

    for chunk in chunks:  # use only every second list item
        totsum += p1(chunk)
    return totsum


with open("i3.txt", 'r') as inp:
    print(p2(inp.read())) # p2 can be swapped for p1
