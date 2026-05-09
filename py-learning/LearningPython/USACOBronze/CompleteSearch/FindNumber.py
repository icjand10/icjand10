def binary_search(numbers, target):
    def search_recursive(start_index, end_index):
        if start_index > end_index:
            return False

        middle_index = (start_index + end_index) // 2
        middle_value = numbers[middle_index]

        if middle_value == target:
            return True

        if target < middle_value:
            return search_recursive(start_index, middle_index - 1)

        return search_recursive(middle_index + 1, end_index)
    
    return search_recursive(0, len(numbers) - 1)
