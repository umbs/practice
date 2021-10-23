"""
The solution is O(N^2). Discussions have good idea about O(N) solution.
"""
from typing import List

class Solution:
    def maxIndex(self, nums: List[int]) -> int:
        hi, idx = nums[0], 0
        for i in range(0, len(nums)):
            if nums[i] > hi:
                hi, idx = nums[i], i
        
        return idx
                
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        hi = self.maxIndex(nums)
        node = TreeNode(nums[hi])
        
        if hi > 0:
            node.left = self.constructMaximumBinaryTree(nums[:hi])
        if hi+1 < len(nums):
            node.right = self.constructMaximumBinaryTree(nums[hi+1:])
        
        return node

