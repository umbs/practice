class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        start, end = s.split(':')
        rs, re = start[1], end[1]
        cs, ce = start[0], end[0]
        idx = rs
        
        result = []
        while cs <= ce:
            while rs <= re:
                result.append(cs + rs)
                rs = chr(ord(rs) + 1)
            
            rs = idx
            cs = chr(ord(cs) + 1)

        return result
