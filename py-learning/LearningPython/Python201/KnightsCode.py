import sys
sys.setrecursionlimit(10000000)

n, m, startX, startY = map(int, input().split())

tours = 0
visited = []
for row in range(n):
    r = []
    for col in range(m):
        r.append(0)
    visited.append(r)

dirX = [2, 1, -1, -2, -2, -1, 1, 2]
dirY = [1, 2, 2, 1, -1, -2, -2, -1]

def isValid(x, y):
    if x < 0 or x >= n:
        return False
    if y < 0 or y >= m:
        return False
    if visited[x][y] != 0:
        return False
    return True

def knightTour(x, y, step):
    global tours
    if not isValid(x, y):
        return

    visited[x][y] = step

    if step == n * m:
        tours += 1
        visited[x][y] = 0
        return

    for direction in range(8):
        nextX = x + dirX[direction]
        nextY = y + dirY[direction]
        knightTour(nextX, nextY, step + 1)

    visited[x][y] = 0

knightTour(startX, startY, 1)
print(tours)
