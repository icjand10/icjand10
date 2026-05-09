n, m = map(int, input().split())
maze = [list(map(int, input().split())) for i in range(n)]

visit = [[0] * m for i in range(n)]
seen = [[False] * m for i in range(n)]
count = [1]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def floodfill(x, y):
  seen[x][y] = True
  visit[x][y] = count[0]
  count[0] += 1

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[1]
    if not seen[nx][ny]:
      floodfill(nx, ny)


for i in range(n):
    print(*visit[i])