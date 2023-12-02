digit_dict = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8',
                 'nine': '9', '1':'1', '2':'2', '3':'3','4':'4', '5':'5', '6':'6','7':'7','8':'8','9':'9'}



def read_first_digit(row):
    for i in range(1, len(row)+1):
        start_of_line = row[:i]

        #check if any key in digit_dict is part of startofline
        for siffra in digit_dict:
            if siffra in start_of_line:
                return digit_dict[siffra]

    return None

def read_last_digit(row):
    for i in range(1, len(row)+1):
        end_of_line = row[-i:]

        # check if any key in digit_dict is part of startofline
        for siffra in digit_dict:
            if siffra in end_of_line:
                return digit_dict[siffra]

    return None



def find_calibration(row: str):
    calibr_str = read_first_digit(row)+read_last_digit(row)
    return int(calibr_str)



with open('input1.txt', 'r') as inp:
    tot_sum = 0
    for line in inp:
        line = line.strip()
        print(line)


        cnr = find_calibration(line)
        print("cn: ", cnr)
        print("______")

        tot_sum += cnr


    print(tot_sum)
