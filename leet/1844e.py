class Solution(object):
    def replaceDigits(self, s: str) -> str:
        chars = list(s)
        for i in range(1, len(s), 2):
            chars[i] = chr(ord(s[i-1]) + int(s[i]))
        return ''.join(chars)

if __name__ == "__main__":
    s = Solution()
    print(s.replaceDigits("a1c1e1"))
    print(s.replaceDigits("a1b2c3d4e"))
    # print(s.replaceDigits())
