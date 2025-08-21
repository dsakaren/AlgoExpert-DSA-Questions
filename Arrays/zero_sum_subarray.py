def zeroSumSubarray(nums):
    # Write your code here.
    for i in range(len(nums)):
        for j in range(len(nums), i, -1):
            subset = nums[i:j]
            if sum(subset) == 0:
                return True

    return False
