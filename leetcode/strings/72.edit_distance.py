def edit_distance(s, t):
    # Create a grid to store the edit distance
    d = [[0 for j in range(len(t) + 1)] for i in range(len(s) + 1)]

    print(d)

    # Initialize the grid
    for i in range(len(s) + 1):
        d[i][0] = i
    print(d)
    for j in range(len(t) + 1):
        d[0][j] = j
    print(d)

    # Iterate over the grid to fill in the edit distance
    for j in range(1, len(t) + 1):
        for i in range(1, len(s) + 1):
            if s[i - 1] == t[j - 1]:
                d[i][j] = d[i - 1][j - 1]
            else:
                d[i][j] = min(d[i - 1][j] + 1, d[i][j - 1] +
                              1, d[i - 1][j - 1] + 1)

    # Return the edit distance
    return d[len(s)][len(t)]


print(edit_distance("horse", "ros"))
print(edit_distance("intention", "execution"))

# print(edit_distance("kitten", "sitting"))
# print(edit_distance("sunday", "saturday"))
# print(edit_distance("saturday", "sunday"))
# print(edit_distance("saturday", "saturday"))
