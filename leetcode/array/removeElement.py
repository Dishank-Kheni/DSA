def removeElement(nums, val):
    for count in range(nums.count(val)):
        nums.remove(val)

    return nums


print(removeElement([3, 2, 2, 3], 3))
