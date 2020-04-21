""" This is O(N^2) solution. Discussions have O(NlogN) solution based on mergesort
https://leetcode.com/problems/create-target-array-in-the-given-order/discuss/549583/O(nlogn)-based-on-%22smaller-elements-after-self%22.
"""
class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        target = []
        
        for i in range(len(nums)):
            target.insert(index[i], nums[i])
        
        return target
