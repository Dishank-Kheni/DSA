def findMedianSortedArrays(num1, num2):
    num1.extend(num2)
    num1.sort()
    if len(num1) % 2 == 0:
        return (num1[len(num1)//2]+num1[len(num1)//2-1])/2
    else:
        return num1[len(num1)//2]


print(findMedianSortedArrays([1, 2], [3, 4]))
