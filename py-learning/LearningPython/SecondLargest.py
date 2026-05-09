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
print(secondlargest([1, 2, 3, 4, 5, 6]))
print(secondlargest([1, 2, 8, 3, 4, 5, 6]))
print(secondlargest([1, 2, 6, 3, 4, 5, 6]))