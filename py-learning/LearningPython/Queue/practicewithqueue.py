from collections import deque
q = deque([4, 2, 3, 1])
qs = deque([])
c = len(q)
def reverseQueue(q):
     for i in range (c):
          qs.appendleft(q.popleft())
reverseQueue(q)
print(qs)


     