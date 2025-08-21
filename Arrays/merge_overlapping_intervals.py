def mergeOverlappingIntervals(intervals):
    # Write your code here.
    if not intervals:
        return []

    intervals.sort(key=lambda v: v[0])

    merged_intervals = [intervals[0]]
    # print(merged_intervals)

    for i in range(1, len(intervals)):
        if intervals[i][0] > merged_intervals[-1][1]:
            merged_intervals.append(intervals[i])
        else:
            merged_intervals[-1][1] = max(merged_intervals[-1][1], intervals[i][1])

    return merged_intervals
