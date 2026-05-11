size = 5
tours = 0
visited = []
for row in range(size):
    r = []
    for col in range(size):
        r.append(0)
    visited.append(r)

dirX = [2, 1, -1, -2, -2, -1, 1, 2]
dirY = [1, 2, 2, 1, -1, -2, -2, -1]

def isValid(x, y):
    if x < 0 or x >= size:
        return False
    if y < 0 or y >= size:
        return False
    if visited[x][y] != 0:
        return False
    return True

def knightTour(x, y, step):
    global tours
    if not isValid(x, y):
        return
    visited[x][y] = step
    if step == size * size:
        tours = tours + 1
        visited[x][y] = 0
        return
    for direction in range(8):
        nextX = x + dirX[direction]
        nextY = y + dirY[direction]

        knightTour(nextX, nextY, step + 1)
    visited[x][y] = 0
knightTour(0, 0, 1)

print(tours)