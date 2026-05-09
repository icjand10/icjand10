x, y = map(int, input().split())

pos = x
step = 1
total = 0

while True:
    next_pos = x + step
    if (pos <= y <= next_pos) or (pos >= y >= next_pos):
        total += abs(y - pos)
        break

    total += abs(next_pos - pos)
    pos = next_pos
    step *= -2 

print(total)
