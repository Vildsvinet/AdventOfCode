
def read_input(filename):
    seeds = []
    maps = []

    current_map = []
    with open(filename, 'r') as inp:
        seeds = parse_seeds(inp.readline())

        for line in inp:
            line = line.strip()
            if line == "" and current_map:
                maps.append(current_map)
                current_map.clear()
                current_map.append(inp.readline())
            elif line == "" and not current_map:
                continue
            else:
                current_map.append(parse_input(line))

    return seeds


def parse_seeds(seed_line: str):  # -> list:
    str_seeds = seed_line.strip().split(':')[1].strip().split(' ')
    return [int(s) for s in str_seeds]


def parse_input(line):
    print(line.split(' '))
    # destination_range_start, source_range_start, range_length = line.split(' ')
    # print(destination_range_start, source_range_start, range_length)
    pass

print(read_input("input5.txt"))

# when empty line, close and add new element to maps
# a, b, c = maps (unpack them again)

# if nr in range(source_range_start, range_length):
#   follow nr

def find_destination_from_source(nr: int, amap) -> int:
    """
    See what
    :param nr:
    :param amap:
    :return:
    """
    next = 0
    return next


def find_location_from_seed(seed: int):
    location = 0
    return location
