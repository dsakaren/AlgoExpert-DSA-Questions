def firstDuplicateValue(array):
    # Write your code here.
    duplicates = []

    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] == array[j]:
                duplicates.append(j)

    if duplicates:
        return array[min(duplicates)]

    return -1
