class Solution(object):
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        def cmp(board, run):
            res = set(board[0]) == set(run[0]) and \
                    set(board[1]) == set(run[1]) and \
                    set(board[2]) == set(run[2])
            if res:
                print(board)
                print(run)
                return True

        def helper(board, run, turn):
            if cmp(board, run):
                return True

            c = 'X' if turn == 0 else 'O'

            for i in range(3):
                for j in range(3):
                    if board[i][j] != run[i][j] and board[i][j] == c:
                        run[i][j] = c
                        res = helper(board, run, (turn+1)%2)

                        if res:
                            return True

            return False

        nb = [list(board[0]), list(board[1]), list(board[2])]
        run = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

        return helper(nb, run, 0)

if __name__ == "__main__":
    s = Solution()
    #board = ["O  ", "   ", "   "]
    #print(s.validTicTacToe(board))
    board = ["XOX", " X ", "   "]
    print(s.validTicTacToe(board))
    #board = ["XXX", "   ", "OOO"]
    #print(s.validTicTacToe(board))
    #board = ["XOX", "O O", "XOX"]
    #print(s.validTicTacToe(board))
