class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        dt = {nums[i]: i for i in range(len(nums))} # O(N)
        ans = 0

        for num in nums:
            if (diff+num) not in dt:
                continue

            if (2*diff+num) not in dt:
                continue

            ans += 1

        return ans
