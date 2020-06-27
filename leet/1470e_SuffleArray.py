class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        res = []
        i, j = 0, n
        while j < len(nums):
            res.append(nums[i])
            res.append(nums[j])
            i += 1
            j += 1
        
        return res

"""
Read these:
https://leetcode.com/problems/shuffle-the-array/discuss/675956/In-Place-O(n)-Time-O(1)-Space-With-Explanation-and-Analysis
https://leetcode.com/problems/shuffle-the-array/discuss/674947/O(1)-space-O(n)-time-detailed-explanation
"""
