class Solution:
    def threeSum(self, nums):
        result = []
        nums.sort()
        import pdb; pdb.set_trace()
        for i in range(len(nums)-2):
            j, k = i+1, len(nums)-1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s < 0:
                    j += 1
                elif s > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])

        return result

if __name__ == "__main__":
    s = Solution()
    print(s.threeSum([-1,0,1,2,-1,-4]))
