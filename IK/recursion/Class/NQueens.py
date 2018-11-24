'''
Instructor's solution
'''

def nqueens(n):
    # 1-D array, tracking row numbers where Queen is placed. Index of the array
    # indicates the column number. Thus, we can get (row, col) from any cell
    board = [-1] * n
    helper(0, board)

def helper(col, board):
    if col == len(board):
        print(str(n) + " Queens placed")
        print(board)
        return

    for i in range(len(board)):
        board[col] = i
        if no_conflicts(col, board):
            helper(col+1, board)

def no_conflicts(col, board):
    for i in range(col):
        # Queen placed on same row as another queen
        if board[i] == board[col]:
            return False

        # Diagonal check. Smart!!
        if (col-i) == abs(board[col] - board[i]):
            return False

    return True
