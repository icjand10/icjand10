def countingliars(x):
    values = [v for _, v in x]   
    min_liars = float('inf')
    for guess in values:
        liars = 0
        for i in range(len(x)):
            op = x[i][0]
            val = x[i][1]
            if op == 'G' and not (guess > val):
                liars += 1
            if op == 'L' and not (guess < val):
                liars += 1
        min_liars = min(min_liars, liars)

    return min_liars
