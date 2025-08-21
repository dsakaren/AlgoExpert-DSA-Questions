def majorityElement(array):
    # Write your code here.
    for i in range(len(array)):
        current_num = array[i]
        current_count = 0
        for j in range(i,len(array)):
            if current_num == array[j]:
                current_count += 1
                if current_count > len(array) // 2:
                    return array[i]

    return -1


