def parse_input(filename):
    with open(filename, 'r') as inp:
        times_strs = inp.readline().strip().split(':')[1].split(' ')
        times = []
        for t in times_strs:
            if t != '':
                times.append(int(t))

        distances_strs = inp.readline().strip().split(':')[1].split(' ')
        distances = []
        for d in distances_strs:
            if d != '':
                distances.append(int(d))

        # print(times, distances)
        races = list(zip(times, distances))
        # print(races)
        return races


def calc_distance(race_time, held_button_time):
    travel_time = race_time - held_button_time
    travel_speed = held_button_time
    distance_travelled = travel_speed * travel_time
    return distance_travelled


def beats_record(distance_travelled, record):
    return distance_travelled > record


def calc_nr_of_ways(race):
    race_time, record = race
    ways_counter = 0
    for i in range(race_time):
        if beats_record(calc_distance(race_time, i), record):
            ways_counter += 1
    return ways_counter


def calc_first(race):
    race_time, record = race
    for i in range(race_time):
        if beats_record(calc_distance(race_time, i), record):
            return i

def calc_last(race):
    race_time, record = race
    for i in range(race_time):
        if beats_record(calc_distance(race_time, race_time - i), record):
            return race_time - i

if __name__ == '__main__':
    # part 1:
    # races = parse_input('input6.txt')
    # tot_prod = 1
    # for race in races:
    #     tot_prod *= (calc_nr_of_ways(race))
    # print(tot_prod)

    one_race = (46857582, 208141212571410)
    one_race_test = (71530, 940200)
    first_beat = calc_first(one_race)
    print(first_beat)
    last_beat = calc_last(one_race)
    print(last_beat)
    print(last_beat-first_beat+1)