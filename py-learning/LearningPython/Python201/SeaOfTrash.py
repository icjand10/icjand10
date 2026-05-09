n, m = map(int, input().split())
grid = [list(map(int, input().strip())) for i in range(n)]
vis = [[False] * m for i in range(n)]
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def dfs(r, c):
    stack = [(r, c)]
    vis[r][c] = True
    size = 1
    while stack:
        x, y = stack.pop()
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not vis[nx][ny] and grid[nx][ny] == 1:
                vis[nx][ny] = True
                stack.append((nx, ny))
                size += 1
    return size
ans = 0
for r in range(n):
    for c in range(m):
        if grid[r][c] == 1 and not vis[r][c]:
            ans = max(ans, dfs(r, c))

print(ans)