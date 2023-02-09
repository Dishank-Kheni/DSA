def largestRectangleArea(heights):
    # return Largest Rectangle in Histogram (LeetCode 84)
    # Time: O(n), Space: O(n)
    stack = []
    max_area = 0
    for i in range(len(heights)):
        while stack and heights[stack[-1]] > heights[i]:
            h = heights[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)
    while stack:
        h = heights[stack.pop()]
        w = len(heights) if not stack else len(heights) - stack[-1] - 1
        max_area = max(max_area, h * w)
    return max_area


print(largestRectangleArea([2, 1, 5, 6, 2, 3]))
print(largestRectangleArea([2, 1, 2]))
