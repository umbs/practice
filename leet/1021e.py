class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res, tmp, cnt = "", "", 0
        for c in S:
            if c == '(':
                cnt += 1
                tmp += c
            else:
                cnt -= 1
                tmp += c
            
            if cnt == 0:
                res += tmp[1:-1]
                tmp = ""
        
        return res
