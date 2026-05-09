def binarysearch(array, target):
    if len(array) == 0:
        return -1
    low = 0
    array = sorted(array)
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

print(binarysearch([5, 3, 1, 4, 2], 3))