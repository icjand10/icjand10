

n, m = map(int, input().split())
maze = [list(map(int, input().split())) for i in range(n)]

visit = [[0] * m for i in range(n)]
seen = [[False] * m for i in range(n)]
count = [1]


if maze[0][0] == 1:
    for i in range(n):
        print(*visit[i])
else:

    moves = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    def floodfill(x, y):
        seen[x][y] = True
        visit[x][y] = count[0]
        count[0] += 1

        for i in range(4):
            dx, dy = moves[i]
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if not seen[nx][ny] and maze[nx][ny] == 0:
                    floodfill(nx, ny)

    floodfill(0, 0)

    for i in range(n):
        print(*visit[i])