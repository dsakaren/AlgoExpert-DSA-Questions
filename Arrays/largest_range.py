def largestRange(array):
    # Write your code here.
    array = get_unique_values(array)

    max_array = []
    max_len = 0
    increment = 1
    left = 0
    right = 1

    while left < len(array) and right < len(array):
        if array[left] + increment == array[right]:
            right += 1
            increment += 1
            continue
        else:
            current_len = len(array[left:right])
            if current_len > max_len:
                max_len = current_len
                max_array = [array[left], array[right-1]]
            left = right
            right += 1
            increment = 1

    current_len = len(array[left:right])
    if current_len > max_len:
        max_array = [array[left], array[right - 1]]

    return max_array


def get_unique_values(arr):
    nums = set()
    for i in range(len(arr)):
        nums.add(arr[i])

    nums = list(nums)
    nums.sort()

    return nums
