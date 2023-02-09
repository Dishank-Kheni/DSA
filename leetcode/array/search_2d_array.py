from math import ceil, floor


def search(matrix, target):

    m = len(matrix)-1
    n = len(matrix[0])-1

    frontRow, fronColumn = 0, 0
    rearRow, rearColumn = m, n
    print(ceil(((m+1) * (n+1))/2))
    # loop = 1 if round(m+1 * n+1) == 1 else ceil((m+1 * n+1)/2)-1
    for _ in range(ceil((m+1 * n+1)/2)):
        if matrix[frontRow][fronColumn] == target:
            return True
        else:
            if fronColumn == n:
                frontRow += 1
            if fronColumn < n:
                fronColumn += 1
            else:
                fronColumn = 0

        if matrix[rearRow][rearColumn] == target:
            return True
        else:
            if rearColumn == 0:
                rearRow -= 1
            if rearColumn > 0:
                rearColumn -= 1
            else:
                rearColumn = n

    return False


# print(search([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))

# print(search([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))

# print(search([[1]], 1))
# print(search([[1], [3], [5]], 0))

# print(search([[1, 1]], 1))
print(search([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 7))
