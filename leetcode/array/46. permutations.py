def permute(nums):
    # Module to find all possible permutations of nums
    # Create a list of permutations

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

            permutation.append(pair1)
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


print(permute([1, 2, 3, 4]))
