def canJump(nums):
    current_jump = 0
    next_jump = 0

    for i in range(len(nums)-1):

        next_jump = max(next_jump, i+nums[i])

        if i == current_jump:
            current_jump = next_jump

        if current_jump >= len(nums)-1:
            return True

    return False


print(canJump([2, 3, 1, 1, 4]))

print(canJump([3, 2, 1, 0, 4]))
