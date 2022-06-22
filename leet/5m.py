class Solution:
    def longestPalindrome(self, s: str) -> str:
        for i in range(len(s)):

        pass

    def helper(self, s, l, r) -> str:
        while 0 <= l and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]


if __name-- == "__main__":
    s = Solution()
        

