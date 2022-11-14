from typing import List

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        total_ways = 0
        row_moves = [1, -1, 0, 0]
        col_moves = [0, 0, 1, -1]

        cells = 0
        max_row = len(grid)
        max_col = len(grid[0])

        for i in range(max_row):
            for j in range(max_col):
                if grid[i][j] in {0, 1, 2}:
                    cells+= 1

        def backtrack(row, col, visited, current_count):
            nonlocal total_ways

            if grid[row][col] == 2 and current_count >= cells:
                total_ways += 1
                return

            for i in range(4):
                r = row + row_moves[i]
                c = col + col_moves[i]

                if 0 <= r < max_row \
                        and 0 <= c < max_col \
                        and  (r, c) not in visited \
                        and grid[r][c] != -1:
                    visited.add((r, c))
                    backtrack(r, c, visited, current_count+1)
                    visited.remove((r, c))


        for r in range(max_row):
            for c in range(max_col):
                if grid[r][c] == 1:
                    visited = set()
                    visited.add((r, c))
                    backtrack(r, c, visited, 1)

                    return total_ways


if __name__ == "__main__":
    s = Solution()
    result = s.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]])
    print(result)
