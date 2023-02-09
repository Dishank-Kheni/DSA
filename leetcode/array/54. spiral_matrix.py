def spiral(matrix):

    list = []
    colLength = len(matrix) - 1
    rowLength = len(matrix[0]) - 1

    if rowLength < 1 or colLength < 1:
        for i in matrix:
            for j in i:
                list.append(j)
        return list

    for i in range(min(colLength, rowLength)):
        topLeftRow, topLeftCol = i, i
        topRightRow, topRightCol = i, (rowLength-i)
        bottomRightRow, bottomRightCol = colLength - i, rowLength-i
        bottomLeftRow, bottomLeftCol = colLength - i, i

        if topLeftCol == topRightCol:
            while(topLeftRow <= bottomLeftRow):
                print(topLeftRow, topLeftCol, end=" ")
                list.append(matrix[topLeftRow][topLeftCol])
                topLeftRow += 1
            break

        if topLeftRow == bottomLeftRow:
            while(topLeftCol <= topRightCol):
                print(topLeftRow, topLeftCol, end=" ")
                list.append(matrix[topLeftRow][topLeftCol])
                topLeftCol += 1
            break

        while(topLeftCol <= topRightCol-1):
            print(topLeftRow, topLeftCol, end=" ")
            list.append(matrix[topLeftRow][topLeftCol])
            topLeftCol += 1
        print()
        while(topRightRow <= bottomRightRow-1):
            print(topRightRow, topRightCol, end=" ")
            list.append(matrix[topRightRow][topRightCol])
            topRightRow += 1
        print()

        while(bottomRightCol >= i+1):
            print(bottomRightRow, bottomRightCol, end=" ")
            list.append(matrix[bottomRightRow][bottomRightCol])
            bottomRightCol -= 1
        print()

        while(bottomLeftRow >= i+1):
            print(bottomLeftRow, bottomLeftCol, end=" ")
            list.append(matrix[bottomLeftRow][bottomLeftCol])
            bottomLeftRow -= 1

    return list


print(spiral([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]))
print(spiral([[1, 11], [2, 12], [3, 13], [4, 14], [5, 15],
              [6, 16], [7, 17], [8, 18], [9, 19], [10, 20]]))
print(spiral([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]))
# print(spiral([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
# print(spiral([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]))
