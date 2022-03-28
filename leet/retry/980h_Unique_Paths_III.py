from  typing import List


"""
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # grid(i,j) = 1 + grid(i±1, j±1) within boundaries and unvisited cells
        return self.helper(grid, 0, 0)

    def helper(self, grid: List[List[int]], i: int, j: int) -> int:
        print(f"Cell: {(i, j)}")
        if not self.valid_cell(grid, i, j):
            return 0

        if grid[i][j] == 2:
            if self.all_cells_covered(grid):
                return 1
            else:
                return 0

        grid[i][j] = 3

        return self.helper(grid, i+1, j) + self.helper(grid, i, j+1) + \
                self.helper(grid, i-1, j) + self.helper(grid, i, j-1)

    def valid_cell(self, grid: List[List[int]], i: int, j: int) -> bool:
        width, height = len(grid), len(grid[0])
        if i < 0 or i == width or j < 0 or j == height:
            print(f"Out of bounds. {(i, j)} is invalid")
            return False

        if grid[i][j] == 3 or grid[i][j] == -1:
            print(f"Visited or Blocked. {(i, j)} is invalid")
            return False

        return True

    def all_cells_covered(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    print(f"Cell {(i, j)} is not covered")
                    return False

        return True
"""

"""
Below solution is from Discussions on LC
"""

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        row_movements = [1, -1, 0, 0] # Possible changes in row index
        col_movements = [0, 0, 1, -1] # Possible changes in row index
        ways = 0 # Answer variable
        max_row = len(grid)
        max_col = len(grid[0])
        total = max_row * max_col # Total number of blocks to cover
        for r in range(max_row):
            for c in range(max_col):
                if grid[r][c] == -1: # Remove the blocks which are obstacles
                    total -= 1

        def backtrack(row, col, visited, current_count): # Current row, col, visited indices and number of blocks traversed so far.
            nonlocal ways
            if grid[row][col] == 2 and current_count >= total: # Breaking conditions met
                ways += 1
                return
            for i in range(4): # 4 Possible movements from a certain row, column index
                r = row + row_movements[i]
                c = col + col_movements[i]
                if 0 <= r < max_row and 0 <= c < max_col and grid[r][c] != -1 and not visited[r][c]: # If the new r, c index is in range, is not an obstacle and is not yet visited
                    visited[r][c] = True # Traverse forward with visited set to true
                    backtrack(r, c, visited, current_count + 1) # DFS traversal
                    visited[r][c] = False # Backtrack by setting visited to false

        for r in range(max_row):
            for c in range(max_col):
                if grid[r][c] == 1: # Starting index found
                    visited = [[False] * max_col for _ in range(max_row)]
                    visited[r][c] = True # Set starting index to True
                    backtrack(r, c, visited, 1) # Start DFS from starting index
                    return ways
        return 0

if __name__ == "__main__":
    s = Solution()
    result = s.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]])
    print(result)
