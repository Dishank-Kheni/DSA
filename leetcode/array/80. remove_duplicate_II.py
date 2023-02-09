def removeDuplicates(nums):
    j, repeateTimes, element = 0, 0, nums[0]

    for val in nums:

        if repeateTimes != 2 and val == element:
            nums[j] = val
            j += 1
            repeateTimes += 1

            continue

        if repeateTimes != 2 and val != element:
            nums[j] = val
            j += 1
            repeateTimes = 1
            element = val
            continue

        if val == element and repeateTimes == 2:
            continue

        if val != element and repeateTimes == 2:
            nums[j] = val
            j += 1
            repeateTimes = 1
            element = val
            continue

    for i in range(j, len(nums)):
        nums.__delitem__(j)

    return (nums, j)


print(removeDuplicates([1, 1, 1, 2, 2, 3]))
print(removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))
