class Solution:
    def addDigits(self, num: int) -> int:
        if num//10 == 0:
            return num
        
        ans = 0
        while num:
            ans += num%10
            num //=10
        
        return self.addDigits(ans)


if __name__ == "__main__":
    s = Solution()
    print(s.addDigits(38))
    print(s.addDigits(0))
