N, M = map(int, input().split())

limit = []
for i in range(N):
    length, speed = map(int, input().split())
    limit += [speed] * length

bessie = []
for i in range(M):
    length, speed = map(int, input().split())
    bessie += [speed] * length

print(max(b - l for b, l in zip(bessie, limit)))
