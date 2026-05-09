def countphotos(petals):
    n = len(petals)
    count = 0
    for i in range(n):
        total = 0
        for j in range(i, n):
            total += petals[j]
            length = j - i + 1
            if total % length == 0:
                avg = total // length
                if avg in petals[i:j + 1]:
                    count += 1
    return count

petals = ([1, 1, 2, 3])
print(countphotos(petals))

petals = ([2, 2, 2, 2])
print(countphotos(petals))

petals = ([1, 2, 3])
print(countphotos(petals))

petals = ([3, 1, 2])
print(countphotos(petals))
