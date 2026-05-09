def ceil_div(a, b):
    return (a + b - 1) // b

T = int(input())
for i in range(T):
    A, B, cA, cB, fA = map(int, input().split())

    needA = max(0, fA - A)
    k = ceil_div(needA, cA)


