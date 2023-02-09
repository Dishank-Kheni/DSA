
def sortColors(nums):

    length = len(nums)
    rearPointer = length-1

    i = 0
    while i <= rearPointer:
        try:
            if nums[i] == 2:
                temp = nums[rearPointer]
                nums[rearPointer] = nums[i]
                rearPointer -= 1
                nums[i] = temp
                # if temp != 2:
                #     i += 1

            if nums[i] == 0:
                temp = nums[i]
                del nums[i]
                nums.insert(0, temp)
                i += 1

            if nums[i] == 1:
                i += 1

        except Exception as e:
            return nums

    return nums


print(sortColors([0]))
print(sortColors([0, 0, 0]))
# print(sortColors([2, 0, 2, 1, 1, 0]))
# print(sortColors([2, 0, 1]))
# print(sortColors([2, 2, 2, 1, 2, 0, 1, 2, 1, 2, 0, 2, ]))
