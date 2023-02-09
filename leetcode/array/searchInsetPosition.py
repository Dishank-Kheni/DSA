def searchInsert(nums, target):
    # Find the index of target number in nums
    for i in range(len(nums)):
        if nums[i] == target:
            return i
        elif nums[i] > target:
            return i


print(searchInsert([1, 3, 5, 6], 5))
print(searchInsert([1, 3, 5, 6], 2))
