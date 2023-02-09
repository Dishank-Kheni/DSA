def longestConsecutive(nums):


    nums.sort()
    print(nums)

    prev_count, max_count, temp = 1, 1, 1

    for i in range(1, len(nums)):
        if nums[i-1] == nums[i]-1:
            temp += 1
        elif nums[i-1] == nums[i]:
            continue
        else:
            prev_count = temp
            temp = 1
            max_count = max(prev_count, max_count)

    return max(temp, max_count)


print(longestConsecutive([100, 4, 200, 1, 3, 2]))
print(longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
