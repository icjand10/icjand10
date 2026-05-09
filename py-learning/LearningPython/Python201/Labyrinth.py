def solve():
    n = int(input().strip())
    grid = []
    for i in range(n):
        grid.append(list(map(int, input().split())))

    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        print(0)
        print(-1)
        return

    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    visited = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(False)
        visited.append(row)

    best_dist = float('inf')

    def dfs_dist(r, c, dist):
        nonlocal best_dist

        if dist >= best_dist:
            return

        if r == n-1 and c == n-1:
            best_dist = dist
            return

        visited[r][c] = True

        for dr, dc in directions:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] == 0:
                dfs_dist(nr, nc, dist + 1)

        visited[r][c] = False

    dfs_dist(0, 0, 1) 

    if best_dist == float('inf'):
        print(0)
        print(-1)
        return

    shortest = best_dist


    visited = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(False)
        visited.append(row)

    def dfs_count(r, c, dist):
        if dist > shortest:
            return 0

        if r == n-1 and c == n-1:
            return 1 if dist == shortest else 0

        visited[r][c] = True
        total = 0

        for dr, dc in directions:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] == 0:
                total += dfs_count(nr, nc, dist + 1)

        visited[r][c] = False
        return total

    count = dfs_count(0, 0, 1)  
    print(count)
    print(shortest)

solve()