class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dt = {}
        for i, num in enumerate(nums):
            if target-num in dt:
                return i, dt[target-num]
            dt[num] = i
