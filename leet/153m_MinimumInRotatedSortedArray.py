from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums)-1

        # [3,4,5,1,2]; lo = 0, hi = 4, IterNo = 1
        while lo < hi:
            mid = (lo + hi)//2
            #  [3,4,5,1,2]; lo = 3, mid = 3, hi = 4, IterNo = 2

            # 1 > 2?
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid

        return nums[lo]

if __name__ == "__main__":
    s = Solution()
    print(s.findMin([3,4,5,1,2]))