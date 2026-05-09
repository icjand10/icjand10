def max_groups(arr):
    even=0
    odd=0
    for x in arr:
        if x%2==0:
            even+=1
        else:
            odd+=1
    groups=0
    need_even=True
    while True:
        if need_even:
            if even>0:
                even-=1
                groups+=1
                need_even=False
            elif odd>=2:
                odd-=2
                groups+=1
                need_even=False
            else:
                break
        else:
            if odd>0:
                odd-=1
                groups+=1
                need_even=True
            else:
                break
    return groups

print(max_groups([1,3,5,7,9,11,13]))
print(max_groups([11,2,17,13,1,15,3]))
print(max_groups([2,4,6,8,10]))
print(max_groups([1,2,3,4,5]))
print(max_groups([1,1,1,1,1,1]))
print(max_groups([2,2,2,2,2,2]))
print(max_groups([1,2,3,4,5,6,7,8]))
print(max_groups([1,2,100]))
print(max_groups([7,7,2,2]))
print(max_groups([1,3,5,2,4,6,7,9,11]))
