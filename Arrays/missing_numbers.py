def missingNumbers(nums):
    # Write your code here.
    new_len = len(nums) + 2

    missing_nums = []

    nums.sort()

    # print(nums)

    for i in range(1,new_len+1):
        if i not in nums:
            missing_nums.append(i)

    return missing_nums
