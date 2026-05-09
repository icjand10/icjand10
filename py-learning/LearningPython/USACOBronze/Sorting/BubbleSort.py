def bubblesort(array):
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
        else:
            pass
    return array

print(bubblesort([1, 5, 2, 4, 6]))
print(bubblesort([6, 5, 2, 3, 1]))
print(bubblesort([6, 1, 2, 3, 1]))
print(bubblesort([6, 5, 2, 3, 1, 4, 5, 2, 5, 7, 3, 5, ]))