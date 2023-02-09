def search(nums, target):
    # Find the index of target number in nums
    for i in range(len(nums)):
        if nums[i] == target:
            return i
        
    return -1
