N, Q = map(int, input().split())
a = list(map(int, input().split()))

sizes = [1]
for i in range(1, N):
    sizes.append(sizes[-1] * 2)

for i in range(1, N):
    if a[i] > 2 * a[i - 1]:
        a[i] = 2 * a[i - 1]

for i in range(Q):
    x = int(input())
    remaining = x
    cost = 0
    ans = 10**30

    for i in range(N - 1, -1, -1):
        cnt = remaining // sizes[i]
        cost += cnt * a[i]
        remaining -= cnt * sizes[i]

        if remaining > 0:
            if cost + a[i] < ans:
                ans = cost + a[i]

    if remaining == 0 and cost < ans:
        ans = cost

    print(ans)
