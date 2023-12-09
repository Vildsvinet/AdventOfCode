import math

def read_input():
    lrinstructions = []
    graph_representation1 = []

    with open("input8.txt", 'r') as inp:
        lrinstructions = list(inp.readline().strip())
        inp.readline()  # read the blank line, do nothing

        graph_representation1 = inp.readlines()
    return lrinstructions, graph_representation1


def node_parser(line):
    line = line.strip()
    node1 = line.split('=')
    name = node1[0].strip()
    ch1 = node1[1].strip("( )")
    left, right = ch1.split(', ')
    return name, (left, right)


def parse_input():
    graph_representation2 = {}

    lrinstructions, graph_representation1 = read_input()
    # print(graph_representation1)

    for line in graph_representation1:
        name, children = node_parser(line)
        graph_representation2[name] = children

    return lrinstructions, graph_representation2


def determine_all_start_nodes(graphrep: dict):
    start_nodes = []
    for node in graphrep:  # iterates over keys
        if node[-1] == 'A':
            start_nodes.append(node)
    print(start_nodes)
    return start_nodes


def determine_all_end_nodes(graphrep: dict):
    end_nodes = []
    for node in graphrep:  # iterates over keys
        if node[-1] == 'Z':
            end_nodes.append(node)
    print(end_nodes)
    return end_nodes


def end_condition_met(node_list: list) -> bool:
    for node in node_list:
        if node[-1] != 'Z':
            return False
    return True


def simple_end_condition_met(node_list: list) -> bool:
    for node in node_list:
        if node[-1] == 'Z':
            return True
    return False


def move_node(lr: str, node_children: tuple):
    left, right = node_children
    if lr == 'L': return left
    if lr == 'R': return right
    raise ValueError("something wrong in lr instructions")
    return None


def find_all_zs(lrinstr: list, node, graphrep: dict):
    checkpoints = []
    current = node
    steps_there = 1
    i = 0
    max_i = len(lrinstr)

    while len(checkpoints) < 25:
        if i == max_i:
            i = 0
        current = move_node(lrinstr[i], graphrep[current])
        if current[-1] == 'Z':
            checkpoints.append((current, steps_there))
            steps_there = 0
        steps_there += 1
        i += 1
    return checkpoints


def find_first_z(lrinstr: list, node, graphrep: dict):
    current = node
    steps_there = 1
    i = 0
    max_i = len(lrinstr)
    while True:
        if i == max_i:
            i = 0
        current = move_node(lrinstr[i], graphrep[current])
        if current[-1] == 'Z':
            break
        steps_there += 1
        i += 1
    return steps_there


def part2(lrinstr: list, graphrep: dict):
    steps = 0
    start_nodes = determine_all_start_nodes(graphrep)
    current_nodes = start_nodes

    i = 0
    max_i = len(lrinstr)
    while not end_condition_met(current_nodes):
        if i == max_i:
            i = 0
        for j, n in enumerate(current_nodes):
            current_nodes[j] = move_node(lrinstr[i], graphrep[n])
        i += 1
        steps += 1
    return steps

def traverser(lrinstr, graphrep):
        steps = 0
        current = graphrep['AAA']

        i = 0
        max_i = len(lrinstr)

        while True:
            print(current)
            if i == max_i:
                i = 0
            if lrinstr[i] == 'L':
                if current[0] == 'ZZZ': steps += 1; break
                current = graphrep[current[0]]
            elif lrinstr[i] == 'R':
                if current[1] == 'ZZZ': steps += 1; break
                current = graphrep[current[1]]
            else:
                raise ValueError("something strange in lr instructions")
            steps += 1
            if steps >= 500000:
                break
            i += 1

        return steps

def main():
    lrinstructions, graph_representation = parse_input()
    # print(part2(lrinstructions, graph_representation))
    # print(lrinstructions, graph_representation)
    start_nodes = determine_all_start_nodes(graph_representation)
    end_nodes = determine_all_end_nodes(graph_representation)
    steps_to_first = []
    for n in range(len(start_nodes)):
        print(start_nodes[n])
        steps_to_first.append(find_first_z(lrinstructions, start_nodes[n], graph_representation))

    tot_res = 1
    for f in steps_to_first:
        tot_res *= f
    print(steps_to_first)
    print(math.lcm(*steps_to_first))
    # end_list = find_all_zs(lrinstructions, start_nodes[1], graph_representation)
    # print(end_list)
    # steps = traverser(lrinstructions, graph_representation)
    # print(steps)

if __name__ == '__main__':
    main()
