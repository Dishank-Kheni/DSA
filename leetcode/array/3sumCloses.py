def threeSumClosest(nums, target):
    # closest sum to target
    nums.sort()
    closestSum = nums[0] + nums[1] + nums[2]
    for i in range(len(nums)-2):
        j = i+1
        k = len(nums)-1
        while j < k:
            sum = nums[i] + nums[j] + nums[k]
            if sum < target:
                # closestSum = sum // max(sum, closestSum)
                j += 1
            elif sum > target:
                # closestSum = sum // min(sum, closestSum)
                k -= 1
            else:
                return sum
            closestSum = sum if abs(
                sum - target) < abs(closestSum - target) else closestSum
    return closestSum


print(threeSumClosest([1, 1, 1, 0], -100))
