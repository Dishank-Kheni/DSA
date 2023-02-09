def merge(intervals):
    # merge all intervals that overlapping
    if len(intervals) <= 1:
        return [intervals[0]]
    list = []
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


# print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
# print(merge([[1, 4], [4, 5]]))
# print(merge([[1, 4], [1, 4]]))
# print(merge([[1, 4], [0, 4]]))

print(merge([[1, 4], [0, 1]]))
print(merge([[1, 4], [2, 3]]))
