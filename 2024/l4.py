# Advent of Code, 2024, day 4
import re

def left_to_right(st: str) -> int:
    return len(re.findall('XMAS', st))


def right_to_left(st: str) -> int:
    return left_to_right(st[::-1])


def construct_columns(longtext) -> list:
    no_of_columns = longtext.index('\n') + 1
    columns = ['' for _ in range(no_of_columns)]
    # print(no_of_columns, len(columns))
    for i in range(no_of_columns):
        for c in longtext[i::no_of_columns]:
            columns[i] += c

    # print(columns)
    return columns


def vertical(longtext: str) -> int:
    counter = 0
    columns = construct_columns(longtext)
    for c in columns:
        counter += left_to_right(c)
        counter += right_to_left(c)
    return counter


def construct_diags(longtext: str) -> list:
    rows : list[str] = content.split('\n')
    no_of_columns = len(rows[0])

    no_of_diags = 2 * no_of_columns - 1

    diags = ['' for _ in range(no_of_diags)]
    anti_diags = ['' for _ in range(no_of_diags)]

    # diagonals
    for rownr, row in enumerate(rows):
        for charnr, char in enumerate(row[::-1]):
            diags[charnr + rownr] += char

    # anti diagonals
    for rownr, row in enumerate(rows):
        for charnr, char in enumerate(row):
            anti_diags[charnr + rownr] += char
    # print(diags+anti_diags)

    return diags + anti_diags


def diagonal(longtext: str):
    counter = 0
    diags = construct_diags(longtext)
    for d in diags:
        counter += left_to_right(d)
        counter += right_to_left(d)
    return counter


with open("i4.txt", 'r') as inp:
    content = inp.read()
    tot = 0
    #left to right
    ltr_content_list = content.split('\n')
    for line in ltr_content_list:
        tot += left_to_right(line)
        tot += right_to_left(line)

    tot += vertical(content)
    tot += diagonal(content)
    print(tot)
