'''
This solution is from discussion sections of the problem: 481 on Leetcode. I
can't find the link now
'''
class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        seq = [1, 2, 2]
        head, num, result = 2, 1, 1
        while len(seq) < n:
            for i in range(0, seq[head]):
                seq.append(num)

                if len(seq) >= n:
                    return result

                if num == 1:
                    result += 1

            num = 3-num
            head += 1

        return result


s = Solution()
print s.magicalString(4)
