def cowgymnastics():
    classsize = ['A', 'B', 'C', 'D']
    ranking = [['A', 'C', 'B', 'D'], ['A', 'C', 'D', 'B']]
    pairs = []
    for i in range(len(classsize) - 1):
        for x in range(i + 1, len(classsize)):
            pairs.append((classsize[i], classsize[x]))

    count = 0

    for a, b in pairs:
        good = 0
        for searching in ranking:
            if searching.index(a) < searching.index(b):
                good += 1
            else:
                break

        if good == len(ranking):
            count += 1

    return count
print(cowgymnastics())
