# testlist = [1]
#
# for i in testlist:
#     print(i)
#     testlist.append(i + 1)
#     if i == 10:
#         break

def values(nr):
    match nr:
        case 7 : return 10
        case 1: return 8
        case _: return nr

def values(mylist: list) -> int:
    # do some calulations
    v = 0
    for m in mylist:
        v+= m
    return v

a = ([7, 4, 2], 56)
b = ([7, 3, 2], 13)

test_list = [a, b]
# test_list.sort(key = lambda tpl: list(map(lambda nr: values(nr), tpl[0])))
test_list.sort(key = lambda tpl: values(tpl[0]))

# print(test_list)


t1 = [3, 4, 2, 1, 3, 3, 3]
print(([t1.count(c) for c in t1]))
