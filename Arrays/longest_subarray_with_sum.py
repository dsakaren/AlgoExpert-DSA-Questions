def longestSubarrayWithSum(array, targetSum):
    # Write your code here.
    max_indexes = []
    max_len = 0

    if sum(array) == targetSum:
        max_indexes = [0, len(array)-1]
        return max_indexes

    left = 0
    right = 0

    while left < len(array) and right < len(array):
        current_substr = array[left:right+1]
        current_sum = sum(current_substr)
        if current_sum < targetSum:
            right += 1
        elif current_sum == targetSum:
            current_len = len(current_substr)
            if current_len > max_len:
                max_len = current_len
                max_indexes = [left, right]
            right += 1
        else:
            left += 1
            right = left

    return max_indexes
