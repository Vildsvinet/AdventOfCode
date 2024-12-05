# Advent of Code, 2024, day 4
import re


def left_to_right(st: str) -> int:
    return len(re.findall('XMAS', st))


def right_to_left(st: str) -> int:
    return left_to_right(st[::-1])


def construct_columns(longtext: str) -> list:
    no_of_columns = longtext.index('\n') + 1
    columns = ['' for _ in range(no_of_columns)]

    for i in range(no_of_columns):
        for c in longtext[i::no_of_columns]:
            columns[i] += c
    return columns


def vertical(longtext: str) -> int:
    counter = 0
    columns = construct_columns(longtext)
    for c in columns:
        counter += left_to_right(c)
        counter += right_to_left(c)
    return counter


def construct_diags(rows: list[str]) -> list:
    no_of_columns = len(rows[0])
    no_of_diags = 2 * no_of_columns - 1

    diags = ['' for _ in range(no_of_diags)]
    anti_diags = ['' for _ in range(no_of_diags)]

    # diagonals
    for rownr, row in enumerate(rows):
        for charnr, char in enumerate(row[::-1]):
            diags[charnr + rownr] += char

    # antidiagonals
    for rownr, row in enumerate(rows):
        for charnr, char in enumerate(row):
            anti_diags[charnr + rownr] += char

    return diags + anti_diags


def diagonal(rows: list[str]):
    counter = 0
    diags = construct_diags(rows)
    for d in diags:
        counter += left_to_right(d)
        counter += right_to_left(d)
    return counter

# part 2
def x_mas(fullcontent):
    tot_count = 0

    rows = content.split('\n')
    nr_of_rows = len(rows)
    row_len = len(rows[0])

    for rownr in range(nr_of_rows - 2):  # range(nr_of_rows - 2)
        for c in range(row_len - 2):
            box = rows[rownr][c:c + 3] + rows[rownr + 1][c:c + 3] + rows[rownr + 2][c:c + 3]
            if (re.search("M.M.A.S.S|M.S.A.M.S|S.M.A.S.M|S.S.A.M.M", box)):
                tot_count += 1

    return tot_count


with open("i4.txt", 'r') as inp:
    content = inp.read()

    # part 1
    tot = 0
    content_list = content.split('\n')
    for line in content_list:
        tot += left_to_right(line)
        tot += right_to_left(line)

    tot += vertical(content)
    tot += diagonal(content_list)
    print(tot)

    # part 2
    print(x_mas(content))
