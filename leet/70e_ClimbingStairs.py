class Solution:
    def climbStairs(self, n: int) -> int:
        if n in (0, 1, 2):
            return n

        pprev, prev = 1, 2
        
        for i in range(3, n+1):
            ans = prev + pprev
            pprev = prev
            prev = ans

        return ans
