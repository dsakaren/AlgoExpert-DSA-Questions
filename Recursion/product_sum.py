def productSum(array, multiplier = 1):
    # Write your code here.
    sum = 0
    for item in array:
        if type(item).__name__ == 'int':
            sum += item
        elif type(item).__name__ == 'list':
            sum += productSum(item, multiplier+1)
    return sum * multiplier

