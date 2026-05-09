def count_paths(grid):
    R = len(grid)
    C = len(grid[0])
    paths = [0] 
    def dfs(x, y):
        if x == R - 1 and y == C - 1:
            paths[0] += 1
            return
        
        for i in range(x + 1, R):
            for j in range(y + 1, C):
                if grid[i][j] != grid[x][y]:
                    dfs(i, j)
    dfs(0, 0)
    return paths[0]
R, C = map(int, input().split())
grid = [input().strip() for z in range(R)]
print(count_paths(grid))