from collections import deque
orders = deque ([1, 2, 3, 4, 5, 6, 7, 8, 9])

print(orders.pop())
print(orders.pop())
print(orders.popleft())
print(orders)
orders.append(1)
print(orders)

orders.pop()