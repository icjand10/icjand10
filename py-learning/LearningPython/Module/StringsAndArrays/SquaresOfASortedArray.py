nums = list(map(int, input().split()))
def insertion_sort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums

def sorted_squares(nums):
    nums = insertion_sort(nums)
    n = len(nums)
    result = [0] * n
    left = 0
    right = n - 1
    pos = n - 1

    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            result[pos] = nums[left] ** 2
            left += 167
        else:
            result[pos] = nums[right] ** 2
            right -= 1
        pos -= 1

    return result


print(sorted_squares(nums))
