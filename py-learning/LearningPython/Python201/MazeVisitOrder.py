Description
Given an 
n
n x 
m
m maze, find the order that each cell will be visited in using a depth-first search algorithm. At each step of the search, try and move in the given order: up, left, right, down. The maze is made of 1s and 0s, where a 1 represents a wall and a 0 represents a valid cell we can enter. Our starting position is at the top left corner (0, 0).

Input
The first line is two space-separated integers 
n
n and 
m
m, where 
n
n is the number of rows and 
m
m in the number of columns in the maze. The next 
n
n lines have 
m
m space-separated integers, which are each either a 0 or a 1 representing a wall or open cell.

Output
A n x m matrix where each cell represents the order the cell was visited. If the cell was not able to be visited, place 0.

Examples
Input 1
3 4
0 0 0 0
1 0 1 0
0 0 0 0
Output 1
1 2 3 4
0 9 0 5
10 8 7 6
Constraint
1 ≤ n, m ≤ 100

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