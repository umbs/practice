class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i, j, pairs = 0, 0, 0
        while True:
            if nums[i] == nums[j]:
                j += 1
            else:
                count = j-i
                pairs += (count * (count - 1))/2
                i = j

            if j >= len(nums):
                break

        count = j-i
        pairs += (count * (count - 1))/2
        return pairs

if __name__ == "__main__":
    s = Solution()
    # print(s.numIdenticalPairs([1,2,3,1,1,3]))
    # print(s.numIdenticalPairs([1,1,1,1]))
    print(s.numIdenticalPairs([1,2, 3]))
