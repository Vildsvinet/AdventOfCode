from enum import Enum


class Dir(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    INVALID = 4


def match_F(direction):
    if direction == Dir.UP:
        return Dir.RIGHT
    elif direction == Dir.LEFT:
        return Dir.DOWN
    else:
        raise Exception("Cannot enter F-pipe like that.")


def match_dash(direction):
    if direction == Dir.RIGHT:
        return Dir.RIGHT
    elif direction == Dir.LEFT:
        return Dir.LEFT
    else:
        raise Exception("Cannot enter -pipe like that.")


def match_vbar(direction):
    if direction == Dir.DOWN:
        return Dir.DOWN
    elif direction == Dir.UP:
        return Dir.UP
    else:
        raise Exception("Cannot enter |pipe like that.")


def match_J(direction):
    if direction == Dir.DOWN:
        return Dir.LEFT
    elif direction == Dir.RIGHT:
        return Dir.UP
    else:
        raise Exception("Cannot enter J-pipe like that.")


def match_L(direction):
    if direction == Dir.DOWN:
        return Dir.RIGHT
    elif direction == Dir.LEFT:
        return Dir.UP
    else:
        raise Exception("Cannot enter L-pipe like that.")


def match_seven(direction):
    if direction == Dir.UP:
        return Dir.LEFT
    elif direction == Dir.RIGHT:
        return Dir.DOWN
    else:
        raise Exception("Cannot enter 7-pipe like that.")


def idx_change(to):
    chng = (0, 0)
    match to:
        case Dir.LEFT:
            chng = (0, -1)
        case Dir.RIGHT:
            chng = (0, 1)
        case Dir.UP:
            chng = (-1, 0)
        case Dir.DOWN:
            chng = (1, 0)
        case _:
            raise Exception("Invalid direction")
    return chng


def move(shape, direction):
    nxt_dir = None
    match shape:
        case 'F':
            nxt_dir = match_F(direction)
        case '-':
            nxt_dir = match_dash(direction)
        case '|':
            nxt_dir = match_vbar(direction)
        case 'J':
            nxt_dir = match_J(direction)
        case 'L':
            nxt_dir = match_L(direction)
        case '7':
            nxt_dir = match_seven(direction)
        case '.':
            raise Exception("Reached a .", direction, shape)
        case _:
            raise Exception("This is not even a pipe..")
    deltas = idx_change(nxt_dir)
    return deltas, nxt_dir


# there will be one S in a 2D array
def find_start(maze):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 'S':
                return (i, j)


def traverse(maze, start_idx):
    # i = 0   # debug counter
    symbol_trail = []
    idx_trail = []
    dir_trail = []

    # startup
    si, sj = start_idx
    symbol_trail.append(maze[si][sj])
    idx_trail.append(start_idx)

    # go downwards from start
    current_index = start_idx
    current_symbol = '|'  # pretend. should later be maze[current_idx]
    current_direction = Dir.DOWN

    while current_symbol != 'S':
        # i += 1  #debug counter

        (di, dj), nxt_direction = move(current_symbol, current_direction)
        next_index = current_index[0] + di, current_index[1] + dj
        ni, nj = next_index
        nxt_symbol = maze[ni][nj]

        current_index = next_index
        current_direction = nxt_direction
        current_symbol = nxt_symbol

        idx_trail.append(current_index)
        symbol_trail.append(current_symbol)
        dir_trail.append(current_direction)

    # print(idx_trail, symbol_trail)
    return idx_trail, symbol_trail, dir_trail


def read_input(filename):
    maze = []
    with open(filename, 'r') as inp:
        for line in inp:
            maze.append(list(line.strip()))
    return maze


def draw_outline(maze, route, symbls):
    outl = []

    for row in range(len(maze)):
        outrow = []
        for col in range(len(maze[row])):
            if (row, col) in route:
                idx = route.index((row, col))
                symbol = symbls[idx]
                outrow.append(symbol)
            else:
                outrow.append('.')
        outl.append(outrow)
    # print(*outl)
    return outl


# print a 2D array
def print_maze(arr):
    for row in arr:
        print(''.join(row))


def direction_of_point_on_curve(point, curve, dirs):
    # print("hej")
    # find the index of the point in the curve
    idx = curve.index(point)
    # return dir[that index]
    return dirs[idx]


def check_if_inside(point, curve, dirs, h, w):
    # arr = [[a0,b0,c0],[a1,b1,c1],[a2,b2,c2]]
    cross_counter_right = 0
    cross_counter_down = 0

    i, j = point

    # check row i to end
    for c in range(j, w):
        if (i, c) in curve and \
                not (direction_of_point_on_curve((i,c), curve, dirs) == Dir.RIGHT \
                or direction_of_point_on_curve((i,c), curve, dirs) == Dir.LEFT):
            cross_counter_right += 1

    # check column j to bottom
    for r in range(i, h):
        if (r, j) in curve and \
                not (direction_of_point_on_curve((r,j), curve, dirs) == Dir.DOWN \
                        or direction_of_point_on_curve((r,j), curve, dirs) == Dir.UP):
            cross_counter_down += 1

    if cross_counter_right % 2 == 0 and cross_counter_down % 2 == 0:
        return False
    elif cross_counter_right % 2 == 1 and cross_counter_down % 2 == 1:
        print(point, "was inside the curve")
        return True
    else:
        # print("indeterminate, think more about")
        return False


# perform check_if_inside for every index in ranges (h,w)
def count_insides(curve, dirs, h, w):
    counter = 0
    for i in range(h):
        for j in range(w):
            if not (i, j) in curve:
                if check_if_inside((i, j), curve, dirs, h, w):
                    counter += 1
    return counter


def main():
    maze = read_input("input10.txt")
    start = find_start(maze)
    idx_trail, symbol_trail, dir_trail = traverse(maze, start)
    print(len(symbol_trail))
    furthest = (len(symbol_trail) - 1) / 2
    print(furthest)
    # print(dir_trail)

    outl = draw_outline(maze, idx_trail, symbol_trail)
    print_maze(outl)

    height = len(maze)
    width = len(maze[0])

    points_inside = count_insides(idx_trail, dir_trail, height, width)
    print(points_inside)


if __name__ == "__main__":
    main()
