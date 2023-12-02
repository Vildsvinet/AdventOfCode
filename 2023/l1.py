
def check_for_substrings_then_replace(string):
    digit_strings = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    success = False
    for substr in digit_strings:
        if substr in string:
            success = True
            return string.replace(substr, digit_strings[substr]), success
    return string, success

def digitize(row: str):
    first_found = False
    last_found = False

    for i in range(3, len(row)):
        if first_found and last_found: return row, True
        if not first_found:
            start_of_line = row[:i]
            start_of_line, success = check_for_substrings_then_replace(start_of_line)
            row = start_of_line+row[i:]
            first_found = success

        if not last_found:
            end_of_line = row[-i:]
            end_of_line, success = check_for_substrings_then_replace(end_of_line)
            row = row[:-i] + end_of_line
            last_found = success


    return row, (first_found and last_found)


def digitize_backward(row :str):
    digit_strings = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7',
                     'eight': '8', 'nine': '9'}
    for i in range(3, len(row)):
        start_of_line = row[-i:]
        for digit in digit_strings:
            if digit in start_of_line:
                row = row.replace(digit, digit_strings[digit])
                return row
    return row

def find_calibration(row: str):
    calibr_str = ''
    # forwards
    for ch in line:
        if ch.isdigit():
            calibr_str += ch
            break

    # backwards
    for ch in line[::-1]:
        if ch.isdigit():
            calibr_str += ch
            break
    return int(calibr_str)



with open('input1.txt', 'r') as inp:
    tot_sum = 0
    for line in inp:
        line = line.strip()
        print("v1: ", line)
        line, _ = digitize(line)
        print("v2: ", line)
        # line = digitize_backward(line)
        # print("v3: ", line)

        cnr = find_calibration(line)
        print("cn: ", cnr)
        print("______")

        tot_sum += cnr


    print(tot_sum)
