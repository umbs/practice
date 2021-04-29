class Solution(object):
    def numberOfMatches(self, n: int) -> int:
        res = 0
        while n > 1:
            if n%2 == 0:
                n = n//2
                res += n
            else:
                n = n-1
                n = n//2
                res += n+1
        
        return res 
 

if __name__ == "__main__":
    s = Solution()
    print(s.numberOfMatches(7))
    print(s.numberOfMatches(14))
    # print(s.numberOfMatches())
