class Solution(object):
    def findNumbers(self, nums):
        c = 0
        for i in nums:
            if (10 <= i and i < 100) or (1000<= i and i < 10000) or (i==100000):
                c += 1
        return c
