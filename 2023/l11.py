import copy


def read_input(filename):
    img = []
    with open(filename, 'r') as inp:
        for line in inp:
            img.append(list(line.strip()))
    return img


def pretty_print(universe):
    # print a 2d array of chars
    for row in universe:
        print(''.join(row))


def row_contains_galaxy(grid, row_nr):
    return '#' in grid[row_nr]


def column_contains_galaxy(grid, col_nr):
    for row in grid:
        if row[col_nr] == '#':
            return True
    return False


def expand_universe(universe):
    # make a copy of the universe so that the in parameter isn't changed
    expanded_universe = copy.deepcopy(universe)
    vertical_expansions = 0
    horisontal_expansions = 0

    # expand vertically
    for i, row in enumerate(universe):
        if not '#' in row:
            # insert a row of . s above
            expanded_universe.insert(i + vertical_expansions, ['.'] * len(row))
            vertical_expansions += 1

    # expand horizontally
    for col in range(len(universe[0])):
        if not column_contains_galaxy(universe, col):
            # insert a column of . s to the right of col
            for r in expanded_universe:
                r.insert(col + horisontal_expansions, '.')
            horisontal_expansions += 1
    return expanded_universe


def shortest_distance(galaxy1, galaxy2):
    # calculate shortest manhattan distance between two galaxies in the 2D array (universe)
    gx1, gy1 = galaxy1
    gx2, gy2 = galaxy2
    return abs(gx2 - gx1) + abs(gy2 - gy1)


def find_galaxy_coordinates(universe):
    # find the coordinates of all galaxies in the universe
    galaxy_coordinates = []
    for i, row in enumerate(universe):
        for j, col in enumerate(row):
            if col == '#':
                galaxy_coordinates.append((i, j))
    return galaxy_coordinates


def find_empty_rows(universe):
    empty_rows = []
    for i, row in enumerate(universe):
        if not '#' in row:
            empty_rows.append(i)
    return empty_rows


def find_empty_cols(universe):
    empty_cols = []
    for col in range(len(universe[0])):
        if not column_contains_galaxy(universe, col):
            empty_cols.append(col)
    return empty_cols


def shortest_path(galaxies):
    nrofpairs = 0
    tot_distance = 0
    # find pairwise distances between all galaxies
    for galaxy in galaxies:
        gal_distance = 0
        # calculate distance to every other
        for gal in galaxies:
            if gal != galaxy:
                nrofpairs += 1
                gal_distance += shortest_distance(galaxy, gal)
        tot_distance += gal_distance
    return tot_distance


def main():
    img = read_input("input11.txt")
    # pretty_print(img)
    print("_______________")
    img_expanded = expand_universe(img)
    # pretty_print(img_expanded)
    galaxy_coords = find_galaxy_coordinates(img_expanded)
    tot_distance = shortest_path(galaxy_coords) / 2

    print(tot_distance)


if __name__ == "__main__":
    main()
    # print(shortest_distance((7,12), (10,9)))
# print(read_input("input11.txt"))
