# Advent of Code, 2024, day 1
with open("i1.txt", 'r') as inp:

    left = []
    right = []

    for l in inp:
        x, y = map(int, l.split())
        left.append(x)
        right.append(y)

    left.sort(reverse=True)
    right.sort(reverse=True)

    # part 1:
    # totsum = 0
    # while left:
    #     totsum += abs(left.pop() - right.pop()) # this will empty the list
    # print(totsum)

    # part 2:
    # sim_score = 0
    # for i in left:
    #     sim_score += i * right.count(i)
    # print(sim_score)
