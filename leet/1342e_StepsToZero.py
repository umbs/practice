class Solution(object):
    def numberOfSteps (self, num):
        """
        :type num: int
        :rtype: int
        """
        steps = 0
        while num:
            if num%2:
                num -= 1
            else:
                num //= 2
            steps += 1
        return steps

if __name__ == "__main__":
    s = Solution()
    print(s.numberOfSteps(14))
