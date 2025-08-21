def isMonotonic(array):
    # Write your code here.
    if len(array) <= 1:
        return True

    for i in range(len(array)-1):
        if array[i] >= array[i+1]:
            if i == len(array) - 2:
                return True
        else:
            break

    for i in range(len(array)-1):
        if array[i] <= array[i+1]:
            if i == len(array) - 2:
                return True
        else:
            break

    return False
