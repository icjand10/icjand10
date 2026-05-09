x = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def twosum(target):
    left = 0
    right = len(x) - 1
    while left < right:
        z = x[left] + x[right]
        if z == target:
            return [left, right]
        if z < target:
            left = left + 1
        else:
            right = right - 1

print(twosum(17))

# O(n)