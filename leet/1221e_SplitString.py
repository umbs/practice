class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, l, r = 0, 0, 0
        for c in s:
            if c == 'L':
                l += 1
            else:
                r += 1
            
            if l == r:
                res += 1
        
        return res
