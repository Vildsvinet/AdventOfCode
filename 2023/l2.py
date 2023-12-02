def max_shown(row):
    row= row.strip()

    max_no_of_reds_shown = 0
    max_no_of_blues_shown = 0
    max_no_of_greens_shown = 0

    # parse row
    game_id = row.split(':')[0].split(' ')[1]
    sets = row.split(':')[1].split('; ')
    for s in sets:
        colors = s.split(',')
        for c in colors:
            c = c.strip()
            number, color = c.split(' ')
            # print(number, color)
            number = int(number)
            if 'blue' in color and number > max_no_of_blues_shown:
                max_no_of_blues_shown = number
            if 'red' in color and number > max_no_of_reds_shown:
                max_no_of_reds_shown = number
            if 'green' in color and number > max_no_of_greens_shown:
                max_no_of_greens_shown = number
    print("id:", game_id, "\tblå:", max_no_of_blues_shown, "\tred:", max_no_of_reds_shown, "\tgrön:", max_no_of_greens_shown)

    return game_id, max_no_of_blues_shown, max_no_of_reds_shown, max_no_of_greens_shown


def is_possible(min_blue_needed, min_red_needed, min_green_needed, blue_in_box, red_in_box, green_in_box):
    return ((min_blue_needed <= blue_in_box) and (min_red_needed <= red_in_box) and (min_green_needed <= green_in_box))


def main():
    blue_in_box, red_in_box, green_in_box = 14, 12, 13
    tot_sum = 0
    with open("input2.txt", 'r') as inp:
        for row in inp:
            game_id, min_blue_needed, min_red_needed, min_green_needed = max_shown(row)
            if is_possible(min_blue_needed, min_red_needed, min_green_needed, blue_in_box, red_in_box, green_in_box):
                print(game_id, "was possible!")
                tot_sum += int(game_id)

    print(tot_sum)

if __name__ == "__main__":
    main()