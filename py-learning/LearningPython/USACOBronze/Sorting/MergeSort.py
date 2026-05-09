def mergesort(array):
    if len(array) <= 1:
        return array
    else:
        half = len(array) // 2
        firsthalf = array[:half]
        secondhalf = array[half:]
        firsthalf = mergesort(firsthalf)
        secondhalf = mergesort(secondhalf)
        return(merging(firsthalf, secondhalf))


def merging(firsthalf, secondhalf):
    merged = []
    a = 0
    b = 0
    while a < len(firsthalf) or b < len(secondhalf):
        if b == len(secondhalf):
            merged.append(firsthalf[a])
            a += 1
        elif  (a < len(firsthalf) and firsthalf[a] <= secondhalf[b]):
            merged.append(firsthalf[a])
            a += 1 
        else:
            merged.append(secondhalf[b])
            b += 1

    return merged


print(mergesort([1, 6, 4, 2, 4, 3]))
print(mergesort([1]))
print(mergesort([1, 6, 4, 2, 4, 3, 4, 3, 2,4 ,65, 7, 4, 3, 45, ]))
