import sys
from time import time

'''
Lot of optimizations can be done. For example, instead of a 2-D board, a 1-D
board can be used to maintain state of the board. See NQueens.py in Class/
folder.

I had board containg strings ('-' and 'q') instead of (0, 1) respectively. But
running time tests showed that managing strings were taking longer (marginally),
as shown below
        strings     ints
n=12    16.70       15.51 
n=13    99.19       97.87 
'''
def add_to_result(board, result):
    lines = list()
    for row in board:
        out = ''.join('-' if r == 0 else 'q' for r in row)
        lines.append(out)

    result.append(lines)


def conflict(row, col, board):
    # check the row
    for i in range(0, col):
        if board[row][i] == 1:
            return True

    # check diagonal 1 - left top
    r, c = row, col
    while r >=0 and c >= 0:
        if board[r][c] == 1:
            return True
        r, c = r-1, c-1

    # check diagonal 2 - left bottom
    r, c = row, col
    while r < len(board) and c >= 0:
        if board[r][c] == 1:
            return True
        r, c = r+1, c-1

    return False 


def helper(n, col, board, result):
    if col == len(board):
        add_to_result(board, result)
        return

    for row in range(0, len(board)):
        if not conflict(row, col, board):
            board[row][col] = 1
            helper(n-1, col+1, board, result)
            board[row][col] = 0

def find_all_arrangements(n):
    result = list()
    board = [[0] * n for _ in range(n)]
    helper(n, 0, board, result)
    return result


if __name__ == "__main__":
    f = sys.stdout

    # n = int(input())
    start = time()
    res = find_all_arrangements(13);
    end = time()
    print(end-start)
   
    '''
    for res_x in res:
        for res_y in res_x:
            f.write(str(res_y) + " ")
        f.write("\n")
    '''
    f.close()
