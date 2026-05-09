nums = list([1, 2, 3, 9, 5, 6, 0, 8])
numsx = nums
def sortorno(nums):
    nums = nums.sort()
    if nums == numsx:
        return True
    else:
        return False
print(sortorno(nums))
   
