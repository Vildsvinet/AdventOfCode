from enum import Enum


class Dir(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    INVALID = 4


def match_F(frm):
    if frm == Dir.DOWN:
        return Dir.RIGHT
    elif frm == Dir.RIGHT:
        return Dir.DOWN
    else:
        raise Exception("Cannot enter F-pipe like that.")


def match_dash(frm):
    if frm == Dir.LEFT:
        return Dir.RIGHT
    elif frm == Dir.RIGHT:
        return Dir.LEFT
    else:
        raise Exception("Cannot enter -pipe like that.")


def match_vbar(frm):
    if frm == Dir.UP:
        return Dir.DOWN
    elif frm == Dir.DOWN:
        return Dir.UP
    else:
        raise Exception("Cannot enter |pipe like that.")


def match_J(frm):
    if frm == Dir.UP:
        return Dir.LEFT
    elif frm == Dir.LEFT:
        return Dir.UP
    else:
        raise Exception("Cannot enter J-pipe like that.")


def match_L(frm):
    if frm == Dir.UP:
        return Dir.RIGHT
    elif frm == Dir.RIGHT:
        return Dir.UP
    else:
        raise Exception("Cannot enter L-pipe like that.")


def match_seven(frm):
    if frm == Dir.DOWN:
        return Dir.LEFT
    elif frm == Dir.LEFT:
        return Dir.DOWN
    else:
        raise Exception("Cannot enter 7-pipe like that.")


def idx_change(to):
    chng = (0, 0)
    match to:
        case Dir.LEFT:
            chng = (-1, 0)
        case Dir.RIGHT:
            chng = (1, 0)
        case Dir.UP:
            chng = (0, -1)
        case Dir.DOWN:
            chng = (0, 1)
        case _:
            raise Exception("Invalid direction")
    return chng


def nxt(frm, shape):
    nxt_dir = None
    match shape:
        case 'F':
            nxt_dir = match_F(frm)
        case '-':
            nxt_dir = match_dash(frm)
        case '|':
            nxt_dir = match_vbar(frm)
        case 'J':
            nxt_dir = match_J(frm)
        case 'L':
            nxt_dir = match_L(frm)
        case '7':
            nxt_dir = match_seven(frm)
        case '.':
            raise Exception("Reached a .", frm, shape)
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


def traverse(maze, start):
    i = 0
    si, sj = start
    trails = []
    current = start
    trails.append(start)
    # start at S, check all adjacent
    # check up:
    next_symbol = maze[si + 1][sj]
    next_dir = Dir.DOWN
    (di, dj), nxt_dir = nxt(next_dir, next_symbol)
    current = si + di, sj + dj
    while current != 'S' and i < 10:
        print(next_symbol)
        i += 1
        ci, cj = current

        trails.append(next_symbol)
        (di, dj), nxt_dir = nxt(next_dir, next_symbol)
        next_symbol = maze[ci][cj]
    print(trails)
    return trails

    # if adjacent is a possible route, add a new trail


def read_input(filename):
    maze = []
    with open(filename, 'r') as inp:
        for line in inp:
            maze.append(list(line.strip()))
    return maze


def main():
    maze = read_input("input10.txt")
    start = find_start(maze)
    trails = traverse(maze, start)


if __name__ == "__main__":
    main()
