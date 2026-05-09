N = int(input())
elsie = []
for z in range(N):
    x = int(input())
    elsie.append(x)
elsie.sort()
used = [False] * (2*N + 1)
for x in elsie:
    used[x] = True
bessie = []
for x in range(1, 2*N + 1):
    if not used[x]:
        bessie.append(x)
i = 0  
j = 0 
wins = 0
while i < N and j < N:
    if bessie[j] > elsie[i]:
        wins += 1
        i += 1
        j += 1
    else:
        j += 1

print(wins)
