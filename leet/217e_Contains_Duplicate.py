class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dt = set()
        for num in nums:
            if num in dt:
                return True
            dt.add(num)

        return False

