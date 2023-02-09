def rotate(matrix):

    length = len(matrix)

    topLeftRow, topLeftColumn = 0, 0
    topRightRow, topRightColumn = 0, length-1
    bottomRightRow, bottomRightColumn = length-1, length-1
    bottomLeftRow, bottomLeftColumn = length-1, 0
    if length == 2:
        topLeft = matrix[topLeftRow][topLeftColumn]
        topRight = matrix[topRightRow][topRightColumn]
        bottomRight = matrix[bottomRightRow][bottomRightColumn]
        bottomLeft = matrix[bottomLeftRow][bottomLeftColumn]
        matrix[topLeftRow][topLeftColumn] = bottomLeft
        matrix[topRightRow][topRightColumn] = topLeft
        matrix[bottomRightRow][bottomRightColumn] = topRight
        matrix[bottomLeftRow][bottomLeftColumn] = bottomRight
        print(matrix)
        return

    for i in range(length-2):

        for j in range(length-1-(i*2)):

            topLeft = matrix[topLeftRow][topLeftColumn]
            topRight = matrix[topRightRow][topRightColumn]
            bottomRight = matrix[bottomRightRow][bottomRightColumn]
            bottomLeft = matrix[bottomLeftRow][bottomLeftColumn]

            matrix[topLeftRow][topLeftColumn] = bottomLeft
            matrix[topRightRow][topRightColumn] = topLeft
            matrix[bottomRightRow][bottomRightColumn] = topRight
            matrix[bottomLeftRow][bottomLeftColumn] = bottomRight

            # print(topLeft, topRight, bottomRight, bottomLeft)

            topLeftColumn += 1
            topRightRow += 1
            bottomRightColumn -= 1
            bottomLeftRow -= 1

        topLeftRow, topLeftColumn = i+1, i+1
        topRightRow, topRightColumn = i+1, length-2-i
        bottomRightRow, bottomRightColumn = length-2-i, length-2-i
        bottomLeftRow, bottomLeftColumn = length-2-i, i+1

    print(matrix)
    # for i in matrix:
    #     for j in i:
    #         print(j, end="  ", )
    #     print()


rotate([[1, 2], [3, 4]])
rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
rotate([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]),
print()
rotate([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15],
       [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]])
