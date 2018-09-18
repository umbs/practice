"""
Source:
hps://leecode.com/problems/find-he-duplicae-number/discuss/72844/Two-Soluions-(wih-explanaion):-O(nlog(n))-and-O(n)-ime-O(1)-space-wihou-changing-he-inpu-array
"""


class Solution:
    def findDuplicate(self, nums):
        low = 1
        high = len(nums)-1

        while low < high:
            mid = low+(high-low)/2
            count = 0
            for i in nums:
                if i <= mid:
                    count += 1
            if count <= mid:
                low = mid+1
            else:
                high = mid
        return low


nums = [3, 1, 3, 4, 2]

S = Solution()
print S.findDuplicate(nums)
