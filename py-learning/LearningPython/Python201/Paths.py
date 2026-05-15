n = int(input())
maze = [list(map(int, input().split())) for z in range(n)]
visited = [[False] * n for g in range(n)]
directions = [(1,0), (-1,0), (0,1), (0,-1)]
def floodfill(x, y):
    if x == n - 1 and y == n - 1:
        return 1
    visited[x][y] = True
    total = 0
    for dx, dy in directions:
        nr, nc = x + dx, y + dy
        if 0 <= nr < n and 0 <= nc < n:
            if maze[nr][nc] == 0 and not visited[nr][nc]:
                total += floodfill(nr, nc)

    visited[x][y] = False
    return total
if maze[0][0] == 1 or maze[n-1][n-1] == 1:
    print(0)
else:
    print(floodfill(0, 0))
