import heapq

def solve():
    num_cows = int(input())
    arrivals = []

    for seniority in range(num_cows):
        arrival_time, eating_time = map(int, input().split())
        arrivals.append((arrival_time, eating_time, seniority))

    arrivals.sort(reverse=True)

    waiting_heap = []
    current_time = 0
    max_wait_time = 0

    while arrivals or waiting_heap:
        if not waiting_heap:
            arrival_time, eating_time, seniority = arrivals.pop()
            current_time = max(current_time, arrival_time)
            heapq.heappush(waiting_heap, (seniority, arrival_time, eating_time))

        while arrivals and arrivals[-1][0] <= current_time:
            arrival_time, eating_time, seniority = arrivals.pop()
            heapq.heappush(waiting_heap, (seniority, arrival_time, eating_time))

        seniority, arrival_time, eating_time = heapq.heappop(waiting_heap)
        wait_time = current_time - arrival_time
        max_wait_time = max(max_wait_time, wait_time)
        current_time += eating_time

    print(max_wait_time)
