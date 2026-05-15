def solve():
    n = int(input)
    maze = []
    for i in range(n):
        maze.append(int(input()))
    sx, sy = 0, 0
    asx, asy = 0, 0
    visited = []
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    numberofpaths = 0
    largest = "inf"
    def number(sx, sy):

        for i in range(directions):
            nx, ny = sx + directions(i), sy + directions(i)
            if not visited(nx, ny) and maze(nx, ny) == "*":
                visited.append(nx, ny)
                sx, sy = nx, ny
                if maze(nx, ny) == maze(n, n):
                    numberofpaths += 1
                    number(sx, sy)
                else:
                    number(nx, ny)
        if numberofpaths == 0:
            return -1

    def shortest(asx, asy):
        length = 0
        for z in range(directions):
            nx, ny = asx + directions(z), asy + directions(z)
            if not visited(nx, ny) and maze(nx, ny) == 0:
                visited.append(nx, ny)
                length += 1
                if maze(nx, ny) == maze(n, n):
                    return length
                if maze(nx, ny) == 1:
                    shortest(asx, asy)
                if length == largest:
                    return -1
                else:
                    shortest(nx, ny)
print(solve())
                

        

            

