class Solution:
    def minimumSum(self, num: int) -> int:
        digits = []
        while num:
            digits.append(num%10)
            num = num//10

        digits.sort()

        return (10*digits[0] + digits[2]) + (10*digits[1] + digits[3])

if __name__ == "__main__":
    s = Solution()
    print(s.minimumSum(2392))
