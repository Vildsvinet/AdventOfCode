


def calculate_deltas(row):
    deltas = []
    for e in range(len(row)-1):
        d = row[e+1] - row[e]
        deltas.append(d)
    return deltas

#
# deltas1 = []
# for row in reports:
#     deltas1.append(calculate_deltas(row))
# print (deltas1)

def procces_report(report):
    history = []
    current = report
    while not all([x==0 for x in current]):
        history.append(current)
        current = calculate_deltas(current)
    history.append(current)
    return history

def extrapolate(history):
    extrap = history.copy()
    extrap.reverse()
    increase = 0
    length = len(extrap)
    for i in range(length):
        last_value = extrap[i][-1]
        extrap[i].append(last_value + increase)
        increase = last_value + increase
    return extrap


def extrapolate_backwards(history):
    extrap = history.copy()
    extrap.reverse()
    increase = 0
    length = len(extrap)
    for i in range(length):
        extrap[i].reverse()
        last_value = extrap[i][0]
        extrap[i].append(last_value + increase)
        increase = last_value + increase
    return extrap



def main():
    reports = []
    histories = []
    extraps = histories.copy()
    extrapolations = []
    lasts = []


    extraps_backw = histories.copy()
    extrapolations_backw = []
    firsts = []

    with open("input9.txt", 'r') as inp:
        for line in inp:
            line = line.strip().split(' ')
            reports.append([int(x) for x in line])

        # print(reports)
    print(histories)
    for report in reports:
        histories.append(procces_report(report))
    # print(histories)

    for history in extraps:
        extrapolations.append(extrapolate(history))
        # print("HAALL", extrapolations)
    # print(histories)

    for extrp in extrapolations:
        # print("hej", extrp)
        lasts.append(extrp[-1][-1])

    for history in extraps_backw:
        extrapolations_backw.append(extrapolate(history))
        print(extrapolations_backw)

    for extrp in extrapolations_backw:
        firsts.append(extrp[-1][-1])

    # print(extrapolations)
    print(sum( lasts))
    print(sum( firsts))


if __name__ == '__main__':
    main()
