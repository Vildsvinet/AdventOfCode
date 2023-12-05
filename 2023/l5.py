def read_input(filename):
    seeds = []
    maps = []

    current_map = []
    with open(filename, 'r') as inp:
        seeds = parse_seeds(inp.readline())

        for line in inp:
            line = line.strip()
            # when empty line, close and add new map to maps
            if line == "" and current_map:
                maps.append(current_map)
                current_map = []
                current_map.append(inp.readline())
            elif line == "" and not current_map:
                current_map.append(inp.readline().strip())
            else:
                current_map.append([int(s) for s in line.split(' ')])
        maps.append(current_map)

    return seeds, maps


def parse_seeds(seed_line: str)-> list:
    """
    Save seed info
    :param seed_line: the first line in the input file, seedstart+range
    :return: a list of tuples called seeds, each with start and range
    """
    seeds = []
    str_seeds = seed_line.strip().split(':')[1].strip().split(' ')

    for i in range(0, len(str_seeds), 2):
        seeds.append((int(str_seeds[i]), int(str_seeds[i+1])))

    return seeds


def find_destination_from_source(nr: int, amap) -> int:
    """
    See what destination a source has
    :param nr: source number
    :param amap: the current map, eg seedtosoil or watertolight
    :return:
    """
    dest = nr  # default: maps to itself if not stated otherwise
    for line in amap[1:]:

        destination_range_start, source_range_start, range_length = line
        if nr in range(source_range_start, source_range_start + range_length):
            offset = nr - source_range_start
            dest = destination_range_start + offset
            break

    return dest


def find_location_from_seed(seed: int, maps: list):
    source = seed
    for i in range(len(maps)):  # this destination is next source
        source = find_destination_from_source(source, maps[i])

    destination = source
    return destination


if __name__ == '__main__':
    seeds, maps = read_input("input5.txt")
    # print(find_destination_from_source(55, maps[0]))
    min_location = 1000000000000
    for seed_tuple in seeds:
        seed_start, seed_range = seed_tuple
        for s in range(seed_start, seed_start+seed_range):
            location = find_location_from_seed(s, maps)
            if location < min_location:
                min_location = location
        break
    print(min_location)
