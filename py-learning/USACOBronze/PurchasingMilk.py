N, K = map(int, input().split())

moveCounts = {}
for z in range(K):
    a, b, c = map(int, input().split())
    key = (a-1, b-1, c-1)
    moveCounts[key] = moveCounts.get(key, 0) + 1

cells = ['O'] * N
bestScore = -1
boardCount = 0

totalBoards = 1 << N

for i in range(totalBoards):
    countO = cells.count('O')
    if countO < 2 or countO == N:
        score = 0
    else:
        score = 0
        for (i, j, k), cnt in moveCounts.items():
            if cells[i] == 'M' and cells[j] == 'O' and cells[k] == 'O':
                score += cnt

    if score > bestScore:
        bestScore = score
        boardCount = 1
    elif score == bestScore:
        boardCount += 1

    for i in range(N):
        if cells[i] == 'O':
            cells[i] = 'M'
            break
        else:
            cells[i] = 'O'

print(bestScore, boardCount)
