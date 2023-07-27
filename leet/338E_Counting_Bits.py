"""
https://leetcode.com/problems/counting-bits/solutions/656849/python-simple-solution-with-clear-explanation/
"""
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        for i in range(1, n+1):
            ans.append(ans[i>>1] + i%2)
        
        return ans
