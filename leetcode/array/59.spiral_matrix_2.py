def spiral(n):

    if n <= 1:
        return [[n]]

    matrix = []

    temp = 1

    for i in range(n):
        list = []
        for j in range(n):
            list.append(temp)
            temp += 1
        matrix.append(list)

    colLength = n - 1
    rowLength = n - 1

    # if rowLength < 1 or colLength < 1:
    #     for i in matrix:
    #         for j in i:
    #             list.append(j)
    #     return list
    temp = 1
    for i in range(min(colLength, rowLength)):
        topLeftRow, topLeftCol = i, i
        topRightRow, topRightCol = i, (rowLength-i)
        bottomRightRow, bottomRightCol = colLength - i, rowLength-i
        bottomLeftRow, bottomLeftCol = colLength - i, i

        if topLeftCol == topRightCol:
            while(topLeftRow <= bottomLeftRow):
                # print(topLeftRow, topLeftCol, end=" ")
                matrix[topLeftRow][topLeftCol] = temp
                temp += 1
                topLeftRow += 1
            break

        if topLeftRow == bottomLeftRow:
            while(topLeftCol <= topRightCol):
                # print(topLeftRow, topLeftCol, end=" ")
                matrix[topLeftRow][topLeftCol] = temp
                temp += 1
                topLeftCol += 1
            break

        while(topLeftCol <= topRightCol-1):
            # print(topLeftRow, topLeftCol, end=" ")
            matrix[topLeftRow][topLeftCol] = temp
            temp += 1
            topLeftCol += 1
        # print()
        while(topRightRow <= bottomRightRow-1):
            # print(topRightRow, topRightCol, end=" ")
            matrix[topRightRow][topRightCol] = temp
            temp += 1
            topRightRow += 1
        # print()

        while(bottomRightCol >= i+1):
            # print(bottomRightRow, bottomRightCol, end=" ")
            matrix[bottomRightRow][bottomRightCol] = temp
            temp += 1
            bottomRightCol -= 1
        # print()

        while(bottomLeftRow >= i+1):
            # print(bottomLeftRow, bottomLeftCol, end=" ")
            matrix[bottomLeftRow][bottomLeftCol] = temp
            temp += 1
            bottomLeftRow -= 1

    return matrix


print(spiral(3))
print(spiral(1))
