def isValidList(list):
    # check list is vaild or not
    for a in list:
        if a == '.':
            continue
        elif list.count(a) > 1:
            return False
    return True


def isValidSuduku(board):
    # check suduku is vaild or not
    for r in range(9):
        list = []
        for i in range(0, 9):
            list.append(board[i][r])
        print(list)
        if not isValidList(list) or not isValidList(board[r]):
            return False
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            list = []
            for m in range(i, i+3):
                for n in range(j, j+3):
                    list.extend(board[m][n])
            if not isValidList(list):
                return False
    return True


print(isValidSuduku([[".", ".", ".", ".", "5", ".", ".", "1", "."], [".", "4", ".", "3", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", "3", ".", ".", "1"], ["8", ".", ".", ".", ".", ".", ".", "2", "."], [
      ".", ".", "2", ".", "7", ".", ".", ".", "."], [".", "1", "5", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", "2", ".", ".", "."], [".", "2", ".", "9", ".", ".", ".", ".", "."], [".", ".", "4", ".", ".", ".", ".", ".", "."]]))
print(isValidSuduku([[".", "1", ".", "5", "2", ".", ".", ".", "."], [".", ".", ".", ".", ".", "6", "4", "3", "."], [".", ".", ".", ".", ".", ".", ".", ".", "."], ["5", ".", ".", ".", ".", ".", "9", ".", "."], [
      ".", ".", ".", ".", ".", ".", ".", "5", "."], [".", ".", ".", "5", ".", ".", ".", ".", "."], ["9", ".", ".", ".", ".", "3", ".", ".", "."], [".", ".", "6", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", ".", "."]]))
