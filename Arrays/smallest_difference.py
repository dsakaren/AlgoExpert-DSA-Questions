def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
    arrayTwo.sort()

    smallest = float('inf')
    nums = [None, None]

    for i in range(len(arrayOne)):
        for j in range(len(arrayTwo)):
            current_diff = abs(arrayOne[i] - arrayTwo[j])
            if current_diff < smallest:
                smallest = current_diff
                nums[0], nums[1] = arrayOne[i], arrayTwo[j]

    return nums
