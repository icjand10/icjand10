def shortestpath(grid):
    n = len(grid)

    if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
        return -1

    visited = []
    for i in range(n):
        rowlist = []
        for j in range(n):
            rowlist.append(False)
        visited.append(rowlist)

    bestdistance = [1000000000]

    moves = [(1,0), (-1,0), (0,1), (0,-1)]

    def dfs(row, col, steps):
        if steps >= bestdistance[0]:
            return

        if row == n - 1 and col == n - 1:
            bestdistance[0] = steps
            return

        for dr, dc in moves:
            nextrow = row + dr
            nextcol = col + dc

            if 0 <= nextrow < n and 0 <= nextcol < n:
                if not visited[nextrow][nextcol] and grid[nextrow][nextcol] == 0:
                    visited[nextrow][nextcol] = True
                    dfs(nextrow, nextcol, steps + 1)
                    visited[nextrow][nextcol] = False

    visited[0][0] = True
    dfs(0, 0, 0)

    if bestdistance[0] == 1000000000:
        return -1
    return bestdistance[0] + 1  
