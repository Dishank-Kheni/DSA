def jump(nums):
    # Module to find the minimum number of jumps to reach the end of the array
    # Initial variables
    jump_count = 0
    current_jump = 0
    next_jump = 0

    # Loop through the list of numbers
    for i in range(len(nums) - 1):

        # Set the next jump to be the current index plus the value at that index
        next_jump = max(next_jump, i + nums[i])

        # If the current index is equal to the current jump, then increment the
        # jump count and set the current jump to the next jump
        if i == current_jump:
            jump_count += 1
            current_jump = next_jump

    return jump_count


# print(jump([2, 3, 1, 1, 4]))s
print(jump([2, 3, 2, 12, 4, 1, 1, 4, 2, 1, 2]))

# # return the minimum number of jumps to reach the last index
# jump = 0
# i = 0
# isMiddleJumped = False
# while i < len(nums)-1:
#     j = nums[i]

#     if i+j >= len(nums)-1:
#         jump += 1
#         break

#     for k in range(1, j+1):
#         if nums[i+k] > nums[i+j]:
#             remain = j-k
#             if nums[i+k] > (remain + nums[i+j]):
#                 jump += 1
#                 i = i+k
#                 isMiddleJumped = True
#                 break

#     if not isMiddleJumped:
#         jump += 1
#         i = i+j
#     # isMiddleJumped = False
#     isMiddleJumped = False
# return jump


# print(jump([1, 2, 3]))
# print(jump([2, 1]))
print(jump([5, 4, 0, 1, 3, 6, 8, 0, 9, 4, 9, 1, 8, 7, 4, 8]))
# print(jump([2, 3, 1, 1, 4]))
# print(jump([2, 3, 0, 1, 4]))
