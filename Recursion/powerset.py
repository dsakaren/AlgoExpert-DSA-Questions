def powerset(array):
    # Write your code here.
    if not array:
        return [[]]

    result = []

    result.append([])

    for num in array:
        temp = len(result)
        for i in range(temp):
            current_sub = result[i] + [num]
            result.append(current_sub)
    return result
