n = int(input())
events = []
for i in range(n):
    a,b = map(int, input().split())
    events.append((a, 1))
    events.append((b, -1))
events.sort()
current = 0
customers = 0
for z, change in events:
    current += change
    customers = max(customers, current)
print(customers)