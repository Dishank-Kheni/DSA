
def firstMissingPositive(nums):
    nums.sort()
    min = 1
    for i in nums:
        if i > 0:
            if min > i:
                min -= 1
            if min < i:
                return min
            min += 1
    return min


# def firstMissingPositive(nums):
#     min = 1
#     nums.sort()
#     firstTime = True
#     for i in nums:
#         if i > 0 and firstTime:
#             min = 1
#             firstTime = False

#         if firstTime == False:
#             if min > i:
#                 min -= 1
#             if min < i:
#                 return min
#             min += 1
#     return min


# print(firstMissingPositive([2, 5, 1, 0]))
# print(firstMissingPositive([1, 2, 0]))
# print(firstMissingPositive([3, 4, -1, 1]))
# print(firstMissingPositive([7, 8, 9, 11, 12]))
# print(firstMissingPositive([1, 1]))
