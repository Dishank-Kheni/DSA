def getPermutation(n, cmp_k):
    k_track = 0
    if n <= 1:
        return [n]

    nums = [i for i in range(1, n+1)]

    # permutation = []

    def recursive_permute(num, rec_per):
        # Recursive function to find all possible permutations of num
        # If the length of num is 1, then append the permutation to the list

        if len(num) == 2:
            nonlocal k_track
            k_track += 1

            print(cmp_k, k_track)
            pair1 = rec_per + num
            if k_track == cmp_k:
                return pair1

            num.reverse()
            k_track += 1
            pair2 = rec_per + num

            if k_track == cmp_k:
                return pair2

            # if pair1 not in permutation:
            #     permutation.append(pair1)

            # if pair2 not in permutation:
            #     permutation.append(pair2)
            return None

        # Loop through the list of numbers
        for k, i in enumerate(num):

            # Create a list of numbers
            num_copy = num[:]

            # Remove the number at index i
            num_copy.pop(k)
            per_copy = rec_per[:]
            per_copy.append(i)
            # Recursively call the function
            result = recursive_permute(num_copy, per_copy,)
            # print(result)
            if result != None:
                return result

    # Call the recursive function
    return recursive_permute(nums, [],).replace("[", "").replace("]", "").replace(",", "").replace(" ", "")

    # return str(permutation[k-1]).replace("[", "").replace("]", "").replace(",", "").replace(" ", "")


# print(getPermutation(3, 3))
print(getPermutation(4, 9))
# print(getPermutation(9, 52))
