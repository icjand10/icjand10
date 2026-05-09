
i = 0
current = [] 

def subsets(arr):
    global i
    global current

    if i == len(arr):
        print(current)
        return

    i += 1
    subsets(arr)
    i -= 1
    current.append(arr[i])
    i += 1
    subsets(arr)
    i -= 1
    current.pop()


print(subsets(['A', 'B', 'C', 'D']))
