n, m = map(int, input().split())
maze = [list(input().strip()) for z in range(n)]
visited = [[False] * m for g in range(n)]
directions = [(1,0), (-1,0), (0,1), (0,-1)]
def floodfill(x, y):
    if x == n - 1 and y == m - 1:
        return 1
    visited[x][y] = True
    total = 0
    for dx, dy in directions:
        nr, nc = x + dx, y + dy
        if 0 <= nr < n and 0 <= nc < m:
            if maze[nr][nc] == '*' and not visited[nr][nc]:
                total += floodfill(nr, nc)
    visited[x][y] = False
    return total
print(floodfill(0, 0))