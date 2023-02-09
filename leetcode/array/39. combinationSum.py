
def combinationSum(candidates, target):
    res = []
    candidates.sort()

    def dfs(remain, stack):
        if remain == 0:
            res.append(stack)
            return

        for item in candidates:
            if item > remain:
                break
            if stack and item < stack[-1]:
                continue
            dfs(remain-item, stack+[item])
    dfs(target, [])
    return res


print(combinationSum([2, 3, 6, 7], 7))

# def combinationSum(candidates, target):
#     # return a list of unique combination which sums equal to target
#     combination = []

#     def divisionRepeat(nums, tar):
#         for num in candidates:
#             remain = tar % num
#             times = tar/num
#             if times < 1.0:
#                 return
#             elif remain == 0:
#                 nums.append([num for i in range(int(times))])
#             else:
#                 divisionRepeat(nums, remain)

#     for num in candidates:

#         250

#         remain = target % num
#         times = target / num

#         if times < 1.0:
#             break
#         elif remain == 0:
#             combination.append([num for i in range(int(times))])
#         else:
#             # pass
#             divisionRepeat([num for i in range(int(times))], remain)

#     return combination


# print(combinationSum([2, 3, 6, 7], 7))
