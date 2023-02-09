def searchRange(nums, target):
    # Find the range of target number in nums

    first, last = -1, -1
    for i in range(len(nums)):
        if nums[i] == target:
            first = i
            j = i
            try:
                while nums[j] == target:
                    j += 1
                last = j-1
            except IndexError:
                last = j-1
            return [first, last]

    return [first, last]


print(searchRange([1], 1))
