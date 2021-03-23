class Solution(object):
    def runningSum(self, nums):
        rs = [nums[0]]
        for i in range(1, len(nums)):
            rs.append(rs[i-1] + nums[i])

        return rs

if __name__ == "__main__":
    s = Solution()
    print(s.runningSum([1,1,1,1,1]))
    print(s.runningSum([3,1,2,10,1]))
