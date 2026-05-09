def countingliars(x):
    liarsL = 0
    liarsG = 0
    for i in range(len(x)):
        operator = x[i][0] # operator can be G or L
        value = x[i][1] # value is a number
        if x[0][0] == 'G':
            for z in range(len(x)):
                if x[i][0] == 'G' and x[z][0] == 'L':
                    if x[i][0] != x[z][0]:
                        if x[i][1] > x[z][1]:
                            liarsG += 1
        else:
            for z in range(len(x)):
                if x[i][0] == 'L' and x[z][0] == 'G':
                    if x[i][0] != x[z][0]:
                        if x[i][1] < x[z][1]:
                            liarsL += 1
    if liarsG < liarsL:
        return liarsG
    else:
        return liarsL
        


# test case 1
x = [['G', 3], ['L', 5]]
print(countingliars(x))

# test case 2
x = [['G', 4], ['L', 3], ['L', 1]]
print(countingliars(x))

x = [['G', 3], ['L', 2]]
print(countingliars(x))

x = [['G', 4], ['L', 3], ['L', 1], ['G', 3], ['L', 2]]
print(countingliars(x))