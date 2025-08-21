def moveElementToEnd(array, toMove):
    # Write your code here.
    array.sort()
    count = 0

    for i in range(len(array)-1, -1, -1):
        if array[i] > toMove:
            count += 1
        else:
            break

    for i in range(len(array)):
        if array[i] == toMove:
            for j in range(0, count):
                array[j+i], array[len(array)-j-1] = array[len(array)-j-1], array[j+i]
            break

    return array
