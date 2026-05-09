

n, m = map(int, input().split())
grid = [list(input().strip()) for i in range(n)]

seen = [[False] * m for i in range(n)]


def dfs(x, y):
    seen[x][y] = True

    for i in range(8):
        dx, dy = moves[i]
        nx, ny = x + dx, y + dy

        if 0 <= nx < n and 0 <= ny < m:
            if not seen[nx][ny] and grid[nx][ny] == '1':
                dfs(nx, ny)

count = 0

for i in range(n):
    for j in range(m):
        if grid[i][j] == '1' and not seen[i][j]:
            dfs(i, j)
            count += 1

print(count)
