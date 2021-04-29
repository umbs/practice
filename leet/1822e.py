from typing import List

class Solution(object):
    def arraySign(self, nums: List[int]) -> int:
        res = 1
        for n in nums:
            if n == 0:
                return 0
            if n < 0:
                res = -res
                
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.arraySign([-1,-2,-3,-4,3,2,1]))
    print(s.arraySign([1,5,0,2,-3]))
    print(s.arraySign([-1,1,-1,1,-1]))
