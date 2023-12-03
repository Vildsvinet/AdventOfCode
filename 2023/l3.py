non_symbols = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '.']

# number, indices of digits in the numbers
# split for .

def process_line(line: str, line_nr: int):
    for ch in line:
        pass

def is_symbol(char):
    return char not in non_symbols

def is_adjacent_to_symbol(index: tuple, matrix: list):
    # if any adjacent is_symbol return True
    i, j = index
    # adjacent elements:
    matrix[i-1][j-1]


def read_file():
    with open("input3.txt", 'r') as inp:
        three_rows_matrix = []
        line_length = 0

        line_nr = 0

        line1 = inp.readline().strip()
        print(line1.split('.'))
        line_length = len(line1)
        three_rows_matrix.append(['.' for _ in range(line_length)])
        three_rows_matrix.append([ch for ch in line1])
        line_nr += 1

        three_rows_matrix.append([ch for ch in inp.readline().strip()])
        line_nr += 1

        print(three_rows_matrix)



        for line in inp:

            line = line.strip()

            process_line(line, line_nr)
            line_nr +=1


def main():
    read_file()

if __name__ == "__main__":
    main()