# from math import factorial

def uniquePaths(m, n):
    dp = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[-1][-1]


print(uniquePaths(23, 12))


# def uniquePaths(m, n):
#     final = []
#     path = 0

#     def tracker(track, node):
#         i, j = node

#         if i < m-1:
#             track.append([i+1, j])
#             tracker(track, [i+1, j]),

#         if j < n-1:
#             track.append([i, j+1])
#             tracker(track, [i, j+1])

#         if i == m-1 and j == n-1:
#             nonlocal path
#             path += 1
#             final.append(track)
#             return

#     # def dfs(i, j):
#     #     if i >= m or j >= n:
#     #         return 0
#     #     if i == m-1 and j == n-1:
#     #         return 1
#     #     return dfs(i+1, j) + dfs(i, j+1)
#     # return dfs(0, 0)

#     # tracker([], [0, 0])

#     return factorial(m+n-2) // factorial(m-1)
#     print(path)
#     return path


# # print(uniquePaths(3, 7))
# # uniquePaths(3, 2)
# print(uniquePaths(23, 12))
