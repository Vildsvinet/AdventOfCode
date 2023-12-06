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


if __name__ == '__main__':
    races = parse_input("input6.txt")
    tot_prod = 1
    for race in races:
        tot_prod *= (calc_nr_of_ways(race))
    print(tot_prod)