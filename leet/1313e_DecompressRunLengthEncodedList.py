class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        out = []
        
        for i in range(0, len(nums), 2):
            for j in range(nums[i]):
                out.append(nums[i+1])
        return out
