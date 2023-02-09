# def maxArea(height):
#     max_area = 0
#     for i in range(len(height)):
#         for j in range(i+1, len(height)):
#             area = min(height[i], height[j]) * (j-i)
#             if area > max_area:
#                 max_area = area
#     return max_area


def maxArea(height):
    max_area = 0
    i = 0
    j = len(height) - 1
    while i < j:
        area = min(height[i], height[j]) * (j-i)
        if area > max_area:
            max_area = area
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return max_area

print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
