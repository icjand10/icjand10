#Diamond Collecter USACO Bronze
N, K = map(int, input().split())
diamonds = [int(input()) for i in range(N)]
diamonds.sort()
left = 0
max_count = 0
for right in range(N):
    while diamonds[right] - diamonds[left] > K:
        left += 1
    max_count = max(max_count, right - left + 1)
print(max_count)
