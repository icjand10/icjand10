N = int(input())
use = [0] * 1001

for i in range(N):
    s, t, b = map(int, input().split())
    for time in range(s, t):
        use[time] += b

print(max(use))
