class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dt = {}
        for c in s:
            dt[c] = 1 + dt.get(c, 0)
        
        for c in t:
            if c not in dt:
                return False
            dt[c] -= 1
        
        for v in dt.values():
            if v != 0:
                return False
        
        return True
