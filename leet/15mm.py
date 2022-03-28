from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        
        def twoSum(nums, target):
            # nums is sorted, can have duplicates
            sz = len(nums)
            i, j = 0, sz-1
            
            # target = 1
            # [-1, 0, 1, 2]
            #   i        j
            
            while i < j:
                add = nums[i] + nums[j]
                if add == target:
                    return nums[i], nums[j]
                elif add < target:
                    i += 1
                else:
                    j -= 1
                    
            return None, None
                
        # [-4, -1, -1, 0, 1, 2]
        #       ^   ----------
        for i, x in enumerate(nums):
            # 2SUM
            y, z = twoSum(nums[i+1:], -x)
            if y is None:
                continue
            else:
                results.append([x, y, z])

if __name__ == "__main__":
    s = Solution()
    result = s.threeSum([-1,0,1,2,-1,-4])
    print(result)
