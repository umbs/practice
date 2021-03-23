class Solution(object):
    def xorOperation(self, n, st):
        ans = 0
        for i in range(n):
            ans ^= (st + 2*i)
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.xorOperation(5, 0))
    print(s.xorOperation(4, 3))
    print(s.xorOperation(1, 7))
