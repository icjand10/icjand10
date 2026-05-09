N, K = map(int, input().split())

moves = []
i = 0
while i < K:
    a, b, c = map(int, input().split())
    moves.append((a-1, b-1, c-1))
    i += 1

depends = []
i = 0
while i < N:
    depends.append([])
    i += 1

i = 0
while i < K:
    x, y, z = moves[i]
    depends[x].append(i)
    depends[y].append(i)
    depends[z].append(i)
    i += 1

cells = ['O'] * N
countO = N

good = [False] * K
score = 0

bestScore = -1
boardCount = 0
totalBoards = 1 << N

def is_good(i):
    x, y, z = moves[i]
    return cells[x] == 'M' and cells[y] == 'O' and cells[z] == 'O'

boards = 0
while boards < totalBoards:

    if score > bestScore:
        bestScore = score
        boardCount = 1
    elif score == bestScore:
        boardCount += 1

    p = 0
    while p < N:
        old = cells[p]

        if old == 'O':
            cells[p] = 'M'
            countO -= 1
            stop = 1
        else:
            cells[p] = 'O'
            countO += 1
            stop = 0

        j = 0
        while j < len(depends[p]):
            mi = depends[p][j]
            before = good[mi]
            after = is_good(mi)
            if before != after:
                good[mi] = after
                if after:
                    score += 1
                else:
                    score -= 1
            j += 1

        if stop == 1:
            break
        p += 1

    boards += 1

print(bestScore, boardCount)
