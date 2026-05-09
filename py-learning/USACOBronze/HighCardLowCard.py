fin = open("cardgame.in", "r")
fout = open("cardgame.out", "w")

n = int(fin.readline())
elsie = [int(fin.readline()) for _ in range(n)]

used = [False] * (2 * n + 1)
for card in elsie:
    used[card] = True

bessie = []
for num in range(1, 2 * n + 1):
    if not used[num]:
        bessie.append(num)

half = n // 2
elsie_high = elsie[:half]
elsie_low = elsie[half:]
bessie_low = bessie[:half]
bessie_high = bessie[half:]

bessie_high.sort()
elsie_high_sorted = sorted(elsie_high)

i = 0
points_high = 0
for e in elsie_high_sorted:
    while i < len(bessie_high) and bessie_high[i] <= e:
        i += 1
    if i < len(bessie_high):
        points_high += 1
        i += 1

bessie_low.sort()
elsie_low_sorted = sorted(elsie_low, reverse=True)

i = len(bessie_low) - 1
points_low = 0
for e in elsie_low_sorted:
    while i >= 0 and bessie_low[i] >= e:
        i -= 1
    if i >= 0:
        points_low += 1
        i -= 1

fout.write(str(points_high + points_low) + "\n")

fin.close()
fout.close()
