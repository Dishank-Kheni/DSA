# 40. Combination Sum II


# def combinationSum2(candidates, target):
#     res = []
#     candidates.sort()

#     def dfs(remain, stack):
#         if remain == 0:
#             if stack not in res:
#                 res.append(stack)
#                 return

#         for item in candidates:
#             if item > remain:
#                 break
#             if stack and item < stack[-1]:
#                 continue
#             dfs(remain-item, stack+[item])
#     dfs(target, [])
#     return res


def combinationSum2(candidates, target):
    res = []
    candidates.sort()

    def dfs(remain, stack, index):
        if remain == 0:
            if stack not in res:
                res.append(stack)
                return

        for i in range(index, len(candidates)):
            if candidates[i] > remain:
                break
            if stack and candidates[i] < stack[-1]:
                continue
            dfs(remain-candidates[i], stack+[candidates[i]], i+1)
    dfs(target, [], 0)
    return res


print(combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))

print(combinationSum2([2, 5, 2, 1, 2], 5))
