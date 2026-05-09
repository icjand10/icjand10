def min_cost(days, K):
    N = len(days)
    cost = K + 1
    end = days[0]
    for i in range(1, N):
        gap = days[i] - end

        if gap > K:
            cost = cost + (K + 1)
        else:
            cost = cost + gap
        end = days[i]

    return cost




print(min_cost([7, 9], 4))

print(min_cost([1, 10], 3)) 

print(min_cost([5], 10))    
print(min_cost([2, 3, 4], 1)) 
print(min_cost([1, 100, 200], 5)) 