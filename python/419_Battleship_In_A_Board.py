def countBattleships(board):
    m = len(board)
    n = len(board[0])
    num = 0
    for i in range(0, m):
        for j in range(0, n):
            if board[i][j] is "X":
                #若上方和左方为空,则该处为船头
                if (i == 0 or board[i - 1][j] is ".") and (j == 0 or board[i][j-1] is "."):
                    num += 1
    return num 