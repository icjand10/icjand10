M, N, K = map(int, input().split())

for i in range(M):
    row = input()
    enlarged = ''.join(c * K for c in row)
    for i in range(K):
        print(enlarged)
