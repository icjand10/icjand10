def solve(maze, x, y, new_value):
    n = len(maze)
    original = maze[x][y]

    if original == new_value:
        return maze
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    def floodfill(x, y):
        maze[x][y] = new_value

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if maze[nx][ny] == original:
                    floodfill(nx, ny)

    floodfill(x, y)
    return maze
