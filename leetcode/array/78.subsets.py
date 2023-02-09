def subsets(nums):
    if len(nums) <= 1:
        return [[], nums]

    subset = []
    subset.append(nums)

    def recursive_subset(num):
        # Recursive function to find all possible subsets of num
        # If the length of num is 1, then append the subset to the list
        if len(num) == 0:
            return

        # Loop through the list of numbers
        for k, i in enumerate(num):

            # Create a list of numbers
            num_copy = num[:]

            # Remove the number at index i
            num_copy.pop(k)
            if num_copy not in subset:
                subset.append(num_copy)
            else:
                continue
            recursive_subset(num_copy)

    # Call the recursive function
    recursive_subset(nums)
    return subset


print(subsets([1, 2, 3, 4, 5, 6, 7, 8, 10, 0]))
