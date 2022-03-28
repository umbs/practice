from math import pow
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        local_max, global_max = -pow(10, 5), -pow(10, 5)
        for i in range(len(nums)):
            local_max = max(nums[i], nums[i] + local_max)
            global_max = max(local_max, global_max)

        return int(global_max)
        
