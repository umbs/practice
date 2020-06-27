class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rs = [nums[0]]
        for i in range(1, len(nums)):
            rs.append(nums[i] + rs[i-1])

        return rs

"""
Solution from discussion forum

ass Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return accumulate(nums)
"""
