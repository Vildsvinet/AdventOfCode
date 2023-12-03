non_symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']

asteriscs = {}


def is_symbol(char):
    return char not in non_symbols


def find_symbols(matrix):
    global symbol_indices
    symbol_indices = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if is_symbol(matrix[i][j]):
                symbol_indices.add((i, j))
                if matrix[i][j] == '*':
                    asteriscs[(i,j)] = []

    return symbol_indices


def adjacent_indices(index, no_of_rows, no_of_columns):
    adjacent_indices = set()
    i, j = index
    if i != 0 and j != 0:
        adjacent_indices.add((i - 1, j - 1))
    if i != 0:
        adjacent_indices.add((i - 1, j))
    if j != 0:
        adjacent_indices.add((i, j - 1))
    if i != no_of_rows - 1 and j != no_of_columns - 1:
        adjacent_indices.add((i + 1, j + 1))
    if i != no_of_rows - 1:
        adjacent_indices.add((i + 1, j))
    if j != no_of_columns - 1:
        adjacent_indices.add((i, j + 1))
    if i != 0 and j != no_of_columns - 1:
        adjacent_indices.add((i - 1, j + 1))
    if i != no_of_rows - 1 and j != 0:
        adjacent_indices.add((i + 1, j - 1))
    return adjacent_indices


def read_file():
    with open("input3.txt", 'r', encoding="UTF-8") as inp:
        return inp.readlines()


def is_adjacent(index, matrix):
    i, j = index
    return (is_symbol(matrix[i - 1][j - 1]) or is_symbol(matrix[i - 1][j]) or is_symbol(matrix[i - 1][j + 1]) \
            or is_symbol(matrix[i][j - 1]) or is_symbol(matrix[i][j + 1]) \
            or is_symbol(matrix[i + 1][j - 1]) or is_symbol(matrix[i + 1][j]) or is_symbol(matrix[i + 1][j + 1]))


def find_number_in_line(line, line_nr, start_at):
    number = '0'
    number_indices = []
    for c in range(start_at, len(line)):
        if (line[c].isdigit()):
            number += line[c]
            number_indices.append((line_nr, c))
            if c == len(line) - 1 or not line[c + 1].isdigit():
                break
    return int(number), number_indices, c + 1


def find_all_numbers_in_line(line, line_nr):
    numbers_on_line = []
    numbers_on_line_indices = []
    start_at = 0
    while start_at <= len(line) - 1:
        found_number, found_number_indices, start_at = find_number_in_line(line, line_nr, start_at)
        numbers_on_line.append(found_number)
        numbers_on_line_indices.append(found_number_indices)

    return numbers_on_line, numbers_on_line_indices


def is_part_number(number, no_of_lines, line_len, symbol_indices):
    value, indices = number
    for i in indices:
        adj = adjacent_indices(i, no_of_lines, line_len)
        if not adj.isdisjoint(symbol_indices):
            nearby_stars = [ind for ind in adj if ind in asteriscs.keys()]
            for star in nearby_stars:
                asteriscs[star].append(value)
            return True
    return False


def main():
    sum_of_part_numbers = 0

    data = [s.strip() for s in read_file()]
    no_of_lines = len(data)  # aka number of rows
    line_len = len(data[0])  # aka number of columns
    # print(data)

    # make a char by char matrix
    elem_matrix = []
    for line in data:
        elem_matrix.append([ch for ch in line])
    # print(elem_matrix)

    symbol_indices = find_symbols(elem_matrix)

    # do the thing
    line_nr = 0
    for line in data:
        numbers_on_line, numbers_on_line_indices = find_all_numbers_in_line(line, line_nr)
        number_candidates = zip(numbers_on_line, numbers_on_line_indices)
        for number_candidate in number_candidates:
            if is_part_number(number_candidate, no_of_lines, line_len, symbol_indices):
                sum_of_part_numbers += number_candidate[0]
        line_nr += 1

    gear_ratio_sum = 0
    print(asteriscs)
    for star in asteriscs:
        if len(asteriscs[star]) == 2:
            gear_ratio_sum += asteriscs[star][0] * asteriscs[star][1]

    print(gear_ratio_sum)

    return sum_of_part_numbers


if __name__ == "__main__":
    print(main())
