def setZeroes(matrix):
    rowLength = len(matrix[0])
    columnLength = len(matrix)
    copy = matrix.copy()

    zeroLocation = []

    for i in range(rowLength):
        for j in range(columnLength):
            if copy[i][j] == 0:
                zeroLocation.append([i, j])

    for i, j in zeroLocation:
        for k in range(columnLength):
            matrix[k][j] = 0
        for k in range(rowLength):
            matrix[i][k] = 0

    # for i in range(rowLength):
    #     for j in range(columnLength):
    #         if copy[i][j] == 0:
    #             for k in range(columnLength):
    #                 matrix[k][j] = 0
    #             for k in range(rowLength):
    #                 matrix[i][k] = 0

    print(matrix)


setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
