non_symbols = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
no_of_lines = 5
line_len = 10
symbol_indices = set()

def is_symbol(char):
    return char not in non_symbols


def find_symbols(matrix):
    global symbol_indices
    #symbol_indices = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if is_symbol(matrix[i][j]):
                symbol_indices.add((i, j))

    return symbol_indices


def adjacent_indices(index, no_of_rows, no_of_columns):
    adjacent_indices = set()
    i, j = index
    if i != 0 and j != 0:
        adjacent_indices.add((i - 1, j - 1))
    if i != 0:
        adjacent_indices.add((1 - i, j))
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


print(adjacent_indices((5, 7), 6, 8))


def read_file():
    with open("input3.txt", 'r') as inp:
        return inp.readlines()


def is_adjacent(index, matrix):
    i, j = index
    return (is_symbol(matrix[i - 1][j - 1]) or is_symbol(matrix[i - 1][j]) or is_symbol(matrix[i - 1][j + 1]) \
            or is_symbol(matrix[i][j - 1]) or is_symbol(matrix[i][j + 1]) \
            or is_symbol(matrix[i + 1][j - 1]) or is_symbol(matrix[i + 1][j]) or is_symbol(matrix[i + 1][j + 1]))


def find_number_in_line(line, start_at):
    number = ''
    number_indices = []
    for c in range(len(line)):
        if (line[c].isdigit()):
            nr1 += line1[c]
            nr1_indices.append((0, c))
            if c+1 == len(line) - 1 or not line1[c + 1].isdigit():
                break
    return int(number), number_indices, c

def find_all_numbers_in_line(line):
    numbers_on_line = []
    numbers_on_line_indices = []
    start_at = 0
    while start_at < len(line)-1:
        found_number, found_number_indices, start_at = find_number_in_line(line, start_at)
        numbers_on_line.append(found_number)
        numbers_on_line_indices.append(found_number_indices)

    return numbers_on_line, numbers_on_line_indices

def is_part_number(number):
    value, indices = number
    for i in indices:
        adj = adjacent_indices(i, no_of_lines, line_len)
        if not adj.isdisjoint(symbol_indices):
            return True
    return False


def main():
    data = [s.strip() for s in read_file()]
    global no_of_lines
    no_of_lines = len(data)  # aka number of rows
    global line_len
    line_len = len(data[0])  # aka number of columns
    print(data)

    # make a char by char matrix
    elem_matrix = []
    for line in data:
        elem_matrix.append([ch for ch in line])
    print(elem_matrix)

    # do the thing
    line1 = data[0]
    nr1 = ''
    nr1_indices = []
    for c in range(line_len):
        if (line1[c].isdigit()):
            nr1 += line1[c]
            nr1_indices.append((0, c))
            try:
                if not line1[c + 1].isdigit(): break
            except IndexError:
                break
    print("number on pos: ", nr1_indices, "")


if __name__ == "__main__":
    main()
