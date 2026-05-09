T = int(input())

for z in range(T):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))

    r = []
    for x in a:
        r.append(x % M)

    r.sort()

    rr = []
    for x in r:
        rr.append(x)
    for x in r:
        rr.append(x + M)

    pref = [0] * (2 * N + 1)
    for i in range(2 * N):
        pref[i+1] = pref[i] + rr[i]

    ans = float('inf')

    i = 0
    while i <= N:
        j = i + N - 1
        mid = (i + j) // 2
        median = rr[mid]

        left_count = mid - i
        left_sum = pref[mid] - pref[i]
        cost_left = median * left_count - left_sum

        right_count = j - mid
        right_sum = pref[j+1] - pref[mid+1]
        cost_right = right_sum - median * right_count

        total_cost = cost_left + cost_right
        if total_cost < ans:
            ans = total_cost

        i += 1

    print(ans)
