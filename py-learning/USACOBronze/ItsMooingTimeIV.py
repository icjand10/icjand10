t, k = map(int, input().split())

for i in range(t):
    N = int(input())
    S = input().strip()

    flip = 0
    keys = []
    ok = True

    for i in range(N - 1, -1, -1):
        c = S[i]

        if flip == 0:
            if c == 'M':
                keys.append('M')
            else:
                keys.append('O')
                flip = 1
        else:
            if c == 'M':
                keys.append('O')
                flip = 0
            else:
                keys.append('M')

    if ok:
        print('YES')
        if k == 1:
            print("".join(reversed(keys)))
    else:
        print('NO')
