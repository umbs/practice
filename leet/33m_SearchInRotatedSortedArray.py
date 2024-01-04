from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)-1

        while lo < hi:
            mid = (lo + hi)//2

            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                if nums[mid] < nums[hi]:
                    lo = mid + 1
                else:



if __name__ == "__main__":
    s = Solution()
    print(s.search([]))