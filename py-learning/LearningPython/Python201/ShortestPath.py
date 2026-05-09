def path(grid):
    n = len(grid)
    if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
        return -1
    visited = []
    for i in range(n):
        arow = []
        for x in range(n):
            arow.append(False)
        visited.append(arow)
    queue = []
    queue.append((0, 0, 1))

    moves = [(1,0), (-1,0), (0,1), (0,-1)]


    while queue:
        row, col, dist = queue.pop(0)

        if row == n - 1 and col == n - 1:
            return dist
        for dr, dc in moves:
            nextrow = row + dr
            nextcol = col + dc
            if 0 <= nextrow < n and 0 <= nextcol < n:
                if not visited[nextrow][nextcol] and grid[nextrow][nextcol] == 0:
                    visited[nextrow][nextcol] = True
                    queue.append((nextrow, nextcol, dist + 1))

    return -1
n = int(input())
inputgrid = []
for f in range(n):
    inputgrid.append(list(map(int, input().split())))

print(path(inputgrid))  


