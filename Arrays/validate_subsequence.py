def isValidSubsequence(array, sequence):
    # Write your code here.
    array.sort()
    sequence.sort()
    # print(array)
    # print(sequence)

    first_num, last_num = sequence[0], sequence[-1]

    for i in range(len(array)):
        if array[i] == first_num:
            left_idx = i
            break
    else:
        return False

    for i in range(len(array)-1, left_idx, -1):
        if array[i] == last_num:
            right_idx = i+1
            break
    else:
        return False

    sub_array = array[left_idx:right_idx]
    count = 0
    for num in sub_array:
        if num in sequence:
            count += 1

    return count == len(sequence)
