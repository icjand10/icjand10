lines = open("bcount.in", "r").readlines()
write = open("bcount.out", "w").write
N, Q = map(int, lines[0].split())
p1 = [0] * (N + 1)
p2 = [0] * (N + 1)
p3 = [0] * (N + 1)
for i in range(1, N + 1):
    b = int(lines[i])  
    p1[i] = p1[i - 1]
    p2[i] = p2[i - 1]
    p3[i] = p3[i - 1]
    if b == 1:
        p1[i] += 1
    elif b == 2:
        p2[i] += 1
    else:
        p3[i] += 1
for z in range(Q):
    a, b = map(int, lines[N + 1 + z].split()) 
    write(str(p1[b] - p1[a - 1]) + " " + str(p2[b] - p2[a - 1]) + " " + str(p3[b] - p3[a - 1]) + "\n")