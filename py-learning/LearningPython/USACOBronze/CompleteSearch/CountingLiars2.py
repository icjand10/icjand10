
def countingliars(list):
    liarsG = 0
    liarsL = 0
    for i in range(len(list)):
        if list[i][0] == 'G':
                for y in range(len(list)):
                    if list[y][0] == 'L':
                        if list[i][1] > list[y][1]:
                            liarsG = liarsG + 1
        else:
            for y in range(len(list)):
                if list[y][0] == 'G':
                    if list[i][1] < list[y][1]:
                        liarsL = liarsL + 1
    if liarsL <= liarsG:
        return liarsL
    elif liarsG < liarsL:
        return liarsG

# test case 1
list = [['G', 3], ['L', 5]]
print(countingliars(list))

# test case 2
list = [['G', 4], ['L', 3], ['L', 1]]
print(countingliars(list))

list = [['G', 3], ['L', 2]]
print(countingliars(list))

list = [['G', 4], ['L', 3], ['L', 1], ['G', 3], ['L', 2]]
print(countingliars(list))