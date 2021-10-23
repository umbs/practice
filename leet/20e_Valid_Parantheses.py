class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ('(', '{', '['):
                stack.append(c)
            else:
                if not stack:
                    return False
                
                left = stack.pop()
                if not self.match(left, c):
                    return False
        
        if stack:
            return False
        
        return True
    
    
    def match(self, a, b):
        if a == '(':
            return b == ')'
        if a == '{':
            return b == '}'
        if a == '[':
            return b == ']'

if __name__ == "__main__":
    s = Solution()
    print(s.isValid("()"))
    print(s.isValid("()[]{}"))
    print(s.isValid("(]"))
    print(s.isValid("([)]"))
    print(s.isValid("{[]}"))
    print(s.isValid("["))

