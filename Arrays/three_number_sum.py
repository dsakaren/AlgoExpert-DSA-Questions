def threeNumberSum(array, targetSum):
    # Write your code here.
    sorted_arr = sorted(array)

    new_array = []

    for i in range(len(sorted_arr)-2):
        if sorted_arr[i] > targetSum:
            break
        for j in range(i+1, len(sorted_arr)-1):
            if sorted_arr[i] + sorted_arr[j] > targetSum:
                break
            for k in range(j+1, len(sorted_arr)):
                if sorted_arr[i] + sorted_arr[j] + sorted_arr[k] > targetSum:
                    break
                if sorted_arr[i] + sorted_arr[j] + sorted_arr[k] == targetSum:
                    new_array.append([sorted_arr[i] , sorted_arr[j], sorted_arr[k]])

    return new_array
