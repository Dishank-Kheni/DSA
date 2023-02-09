def nextPermutation(nums):
    # Find the next big permutation from nums
    tempNum = nums[:]
    nums.sort()
    isNext = False
    for i in nums:
        tempList = nums[:]
        tempList.remove(i)
        for j in range(len(tempList)-1):
            if isNext:
                nums = [i, tempList[j], tempList[j+1]]
                return nums
            if [i, tempList[j], tempList[j+1]] == tempNum:
                nums = [i, tempList[j+1], tempList[j]]
                return nums
            elif [i, tempList[j+1], tempList[j]] == tempNum:
                isNext = True
                # break

            # permutation.append([i, tempList[j], tempList[j + 1]])
            # permutation.append([i, tempList[j+1], tempList[j]])
    # print(permutation)
    # index = permutation.index(tempNum)
    # nums = permutation[index+1] if index != 5 else permutation[0]
    return nums

print(nextPermutation([1, 5, 1]))
