def conflict(board, col):
    '''
    True if there's a conflict in placing a Queen in col and False otherwise
    '''
    for i in range(col):
        if board[i] == board[col]:
            return True



def helper(n, col, board, result):
    pass

def find_all_arrangements(n):
    result = list()
    board = set()
    helper(n, 0, board, result)
