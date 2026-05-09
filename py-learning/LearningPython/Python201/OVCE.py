import sys
sys.setrecursionlimit(999999)
R, C = map(int, input().split())
grid = [list(input()) for z in range(R)]
visited = [[False] * C for f in range(R)]

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
sheep_total = 0
wolf_total = 0

def dfs(r, c):
    visited[r][c] = True
    sheep = 0
    wolves = 0

    if grid[r][c] == "o":
        sheep += 1
    elif grid[r][c] == "v":
        wolves += 1

    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < R and 0 <= nc < C:
            if not visited[nr][nc] and grid[nr][nc] != "#":
                s, w = dfs(nr, nc)
                sheep += s
                wolves += w

    return sheep, wolves

for i in range(R):
    for j in range(C):
        if grid[i][j] != "#" and not visited[i][j]:
            s, w = dfs(i, j)
            if s > w:
                sheep_total += s
            else:
                wolf_total += w

print(sheep_total, wolf_total)