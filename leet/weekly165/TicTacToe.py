class Solution(object):
    def tictactoe(self, moves):
        grid = [[" " for i in range(3)] for j in range(3)]

        for l in moves:
            i, j = l[0], l[1]
            if (i+j) % 2 == 0:
                c = 'X'
            else:
                c = 'O'

            grid[i][j] = c

        return self.status(grid)

    def status(self, grid):
        pass


if __name__ == "__main__":
    s = Solution()
    moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
    # moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
    # moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
    # moves = [[0,0],[1,1]]

    print s.tictactoe(moves)
