with open("lemonade.in", "r") as fin:
    data = fin.read().strip().split()
    N = int(data[0])
    w = list(map(int, data[1:]))

w.sort()
line = 0

for tolerance in reversed(w):
    if line <= tolerance:
        line += 1

with open("lemonade.out", "w") as fout:
    fout.write(str(line) + "\n")
