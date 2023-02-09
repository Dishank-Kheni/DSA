def permuteUnique(nums):
    # return all the possible unique permutation of given nums
    if len(nums) <= 1:
        return [nums]

    permutation = []

    def recursive_permute(num, rec_per):
        # Recursive function to find all possible permutations of num
        # If the length of num is 1, then append the permutation to the list
        if len(num) == 2:
            pair1 = rec_per + num
            num.reverse()
            pair2 = rec_per + num

            if pair1 not in permutation:
                permutation.append(pair1)

            if pair2 not in permutation:
                permutation.append(pair2)
            return

        # Loop through the list of numbers
        for k, i in enumerate(num):

            # Create a list of numbers
            num_copy = num[:]

            # Remove the number at index i
            num_copy.pop(k)
            per_copy = rec_per[:]
            per_copy.append(i)
            # Recursively call the function
            recursive_permute(num_copy, per_copy)

    # Call the recursive function
    recursive_permute(nums, [])
    return permutation


print(permuteUnique([1, 2, 3, 4]))
