class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        running_sum = max_so_far = nums[0]
        for num in nums[1:]:
            running_sum = max(num, num + running_sum)
            max_so_far = max(running_sum, max_so_far)
            
        return max_so_far
