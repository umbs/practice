class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        while True:
            nums = []
            while n:
                nums.append(n%10)
                n = n//10
            if frozenset(nums) in seen:
                return False
           
            n = sum([i*i for i in nums])

            if n == 1:
                return True
            else:
                seen.add(frozenset(nums))


if __name__ == "__main__":
    s = Solution()
    print(s.isHappy(19))
    print(s.isHappy(21))
    print(s.isHappy(101))
    print(s.isHappy(121))
