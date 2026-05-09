def is_sorted_ascending(lst):
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    if len(lst) < 2:
        return True
    i, j = 0, 1
    while j < len(lst):
        if lst[i] > lst[j]:
            return False
        i += 1
        j += 1
    return True
print(is_sorted_ascending([1, 2, 3, 4]))   
print(is_sorted_ascending([1, 3, 2, 4]))   
print(is_sorted_ascending([]))             
print(is_sorted_ascending([5])) 
