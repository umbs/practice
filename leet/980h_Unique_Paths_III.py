""" 2nd attempt. Still not working.

1   0   0   0
0   0   0   0
0   0   2  -1
"""
from typing import List

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        max_row, max_col = len(grid), len(grid[0])
        row_moves = [-1, 1, 0, 0]
        col_moves = [0, 0, -1, 1]

        def helper(r: int, c: int, grid: List[List[int]]) -> int:

            ans = 0

            # Found end node
            if grid[r][c] == 2:
                return 1

            for i in range(4):
                x, y = r+i, c+i
                if 0 <= x < max_row and 0 <= y < max_col and grid[x][y] != 3 and grid[x][y] != -1:

                    num = grid[x][y]
                    grid[x][y] = 3
                    ans += helper(x, y, grid)
                    grid[x][y] = num

            return ans

        for i in range(max_row):
            for j in range(max_col):
                if grid[i][j] == 1:
                    grid[i][j] = 3
                    ans = helper(i, j, grid)
                    grid[i][j] = 1

        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]]))
    print(s.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,0,2]]))
