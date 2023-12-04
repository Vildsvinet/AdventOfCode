testlist = [1]

for i in testlist:
    print(i)
    testlist.append(i+1)
    if i == 10:
        break

