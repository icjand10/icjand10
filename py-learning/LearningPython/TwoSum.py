x = list([1, 2, 3, 4, 5, 6, 7, 8, 9])
def twosum(target):
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            if x[i] + x[j] == target:
                return [i, j]
print(twosum(17))

# n* ((n-1) + (n-2) + (n-3) .... 0)
# = n * ( cN - c)
# = n*n
# = O(n^2)