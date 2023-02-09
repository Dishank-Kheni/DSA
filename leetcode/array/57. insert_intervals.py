def insert(intervals, newIntervals):
    # insert new interval into intervals
    if len(intervals) <= 1:
        return [intervals[0]]
    list = []
    intervals.append(newIntervals)
    # print(intervals)
    intervals.sort()
    prevStart, prevEnd = intervals[0]

    # print(intervals)
    intervals.remove([prevStart, prevEnd])
    for start, end in intervals:
        if prevEnd >= start and prevEnd <= end:
            prevEnd = end
            prevStart = min(start, prevStart)
        elif prevEnd >= start and prevEnd > end:
            continue
        else:
            list.append([prevStart, prevEnd])
            prevStart, prevEnd = start, end

    list.append([prevStart, prevEnd])
    return list


print(insert([[1, 3], [6, 9]], [2, 5]))

print(insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
