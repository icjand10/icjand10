file = open("div7.in", "r")
data = file.read().strip().split()
N = int(data[0])
ids = list(map(int, data[1:]))
first = [-1] * 7
last = [-1] * 7
prefix = 0
for i in range(N):
    prefix = (prefix + ids[i]) % 7
    if first[prefix] == -1:
        first[prefix] = i
    last[prefix] = i
best = 0
for z in range(7):
    if first[z] != 1:
        best = max(best, last[z] - first[z])
print = open("div7.out", "w")
print.write(str(best) + "\n")