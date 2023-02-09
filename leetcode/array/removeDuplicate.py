def removeDuplicates(nums):
    # remove duplicate item from array

    nums.sort()
    j = 0

    for i in range(len(nums)-1):
        if nums[i] != nums[i+1]:
            nums[j] = nums[i]
            j += 1
    nums[j] = nums[len(nums)-1]

    for i in range(j+1, len(nums)):
        nums.__delitem__(j+1)

    # filter(lambda x: x != nums[len(nums)-1], nums)
    # nums.__delitem__(0)
    return nums


print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
