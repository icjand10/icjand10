import math
def fibonacci(n):
    x = 1
    f = x
    v = 1
    c = v
    for i in range((n)):
        print(v)
        v = c + v
        c = v + c

        print(x)
        f = x + f
        x = x + f

print(fibonacci(6))