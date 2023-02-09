def solve(board):
    if not board:
        return

    def dfs(board, i, j):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != 'O':
            return
        board[i][j] = '1'
        dfs(board, i + 1, j)
        dfs(board, i - 1, j)
        dfs(board, i, j + 1)
        dfs(board, i, j - 1)

    m, n = len(board), len(board[0])
    for i in range(m):
        for j in range(n):
            if (i in [0, m - 1] or j in [0, n - 1]) and board[i][j] == 'O':
                dfs(board, i, j)
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            if board[i][j] == '1':
                board[i][j] = 'O'

    return board


print(solve([["X", "X", "X", "X"], ["X", "O", "O", "X"],
      ["X", "X", "O", "X"], ["X", "O", "X", "X"]]))

print(solve([["X", "O", "X", "O"]]))
print(solve([["X"], ["O"], ["X"], ["O"]]))

print(solve([["O"]]))
