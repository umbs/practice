class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = [0] * 102
        for n in nums:
            count[n+1] += 1
        
        for i in range(1, 101):
            count[i] += count[i-1]
        
        return [count[n] for n in nums]
