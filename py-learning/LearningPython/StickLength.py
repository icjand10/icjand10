stick_count = int(input())
lengths = list(map(int, input().split()))

lengths.sort()
median_length = lengths[stick_count // 2]

total_cost = 0
for current_length in lengths:
    total_cost += abs(current_length - median_length)

print(total_cost)
