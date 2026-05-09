def longest_ski_path(grid):
    n = len(grid)
    m = len(grid[0])

    longest = [[0] * m for a in range(n)]
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def dfs(x, y):
        if longest[x][y] != 0:
            return longest[x][y]

        longest[x][y] = 1 

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if grid[nx][ny] < grid[x][y]:
                    longest[x][y] = max(longest[x][y], 1 + dfs(nx, ny))

        return longest[x][y]

    ans = 0
    for i in range(n):
        for j in range(m):
            ans = max(ans, dfs(i, j))

    return ans



R, C = map(int, input().split())
grid = [list(map(int, input().split())) for z in range(R)]
print(longest_ski_path(grid))