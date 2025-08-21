def underscorifySubstring(string, substring):
    # Write your code here.
    indexes = []
    indexes_as_array = []
    left = 0
    inc = len(substring)
    right = left + inc
    output_string = ''

    while left < len(string) and right < len(string):
        current_substring = string[left:right]
        if current_substring == substring:
            indexes.append([left, right])
        left += 1
        right += 1
        current_substring = ''

    current_substring = string[left:right]

    if current_substring == substring:
        indexes.append([left, right])

    indexes = mergeOverlappingIntervals(indexes)

    if not indexes:
        return string

    indexes_as_array = unpack_indexes(indexes)

    output_string = create_output_string(string, indexes_as_array)

    # print(output_string)

    return output_string

def create_output_string(string, arr):
    return_string = ''
    i = 0
    j = 0

    while i < len(string):
        if i in arr:
            return_string += '_'
            arr[j] = ''
            i -= 1
            j += 1
        else:
            return_string += string[i]
        i += 1

    if arr[-1] != '':
        return_string += '_'

    return return_string

def unpack_indexes(intervals):
    new_arr = []
    for i in range(len(intervals)):
        for j in range(len(intervals[i])):
            new_arr.append(intervals[i][j])
    return new_arr

def mergeOverlappingIntervals(intervals):

    if not intervals:
        return []

    merged_intervals = [intervals[0]]

    for i in range(1, len(intervals)):
        if intervals[i][0] > merged_intervals[-1][1]:
            merged_intervals.append(intervals[i])
        else:
            merged_intervals[-1][1] = max(merged_intervals[-1][1], intervals[i][1])

    return merged_intervals
