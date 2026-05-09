def dontbelast(cows):

    if len(cows) > len(set([c[0] for c in cows])):

        for i in range(len(cows) - 1):
            for z in range(i + 1, len(cows)):
                if cows[i][0] == cows[z][0]:
                    cows[i][1] = cows[i][1] + cows[z][1]
                    cows.pop(z)
                    break

        return secondlargest([v[1] for v in cows])

    else:
        return secondlargest([v[1] for v in cows])


def secondlargest(values):

    if values[0] > values[1]:
        largest, second = values[0], values[1]
    elif values[0] < values[1]:
        largest, second = values[1], values[0]
    else:
        largest = values[0]
        second = float('-inf')

    for i in range(2, len(values)):
        n = values[i]

        if n > largest:
            second = largest
            largest = n

        elif largest > n > second:
            second = n

    return second


print(dontbelast([[1, 1], [2, 13], [3, 3], [3, 4], [4, 4], [5, 12], [6, 7], [8, 10], [1, 6], [4, 5]]))
