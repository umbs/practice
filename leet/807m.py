class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
 
        col_max = []
        for c in range(C):
            elem = max([grid[i][c] for i in range(R)])
            col_max.append(elem)

        row_max = []
        for r in range(R):
            elem = max([grid[r][i] for i in range(C)])
            row_max.append(elem)


        ans = 0
        for i in range(R):
            for j in range(C):
                peak = min(row_max[i], col_max[j])
                ans += peak - grid[i][j]
        
        return ans

""" Following solutioin is super elegant. Same as above, but very concise
written in Pythonic manner
https://leetcode.com/problems/max-increase-to-keep-city-skyline/discuss/120681/C++JavaPython-Easy-and-Concise-Solution/146567

"""
