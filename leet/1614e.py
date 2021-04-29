class Solution(object):
    def maxDepth(self, s):
        ans, i = 0, 0
        for c in s:
            if c == '(':
                i += 1
                ans = max(ans, i)
            elif c == ')':
                i -= 1
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.maxDepth("(1+(2*3)+((8)/4))+1"))
    print(s.maxDepth("(1)+((2))+(((3)))"))
    print(s.maxDepth("1+(2*3)/(2-1)"))
    print(s.maxDepth("1"))
