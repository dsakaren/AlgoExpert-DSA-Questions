def arrayOfProducts(array):
    # Write your code here.
    new_array = []

    return_array = [None] * len(array)

    subset = array[1:]

    new_array.append(subset)

    for i in range(1, len(array)):
        curr_num = array.pop(1)
        array.append(curr_num)
        subset = array[0:len(array)-1]
        new_array.append(subset)

    for i in range(len(new_array)):
        return_array[i] = multiple_items(new_array[i])

    return return_array

def multiple_items(iter):
    result = 1
    for i in iter:
        result *= i

    return result
