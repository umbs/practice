class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dt = dict()
        for c in s:
            count = dt.get(c, 0)
            dt[c] = 1 + count
        
        for c in t:
            if c not in dt:
                return False
            
            dt[c] -= 1
            if dt[c] < 0:
                return False
            
        for k, v in dt.items():
            if v > 0:
                return False
        
        return True
