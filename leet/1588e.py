class Solution(object):
    def sumOddLengthSubarrays2(self, arr):
        """ This is super slow algo. We are recounting in every sub-array.
        """
        ans = 0
        diff = 1
        while diff <= len(arr):
            for i in range(len(arr)-diff+1):
                ans += sum(arr[i:i+diff])
           
            diff += 2

        return ans

    def sumOddLengthSubarrays(self, arr):
        ans, diff, add = 0, 1, [arr[0]]

        # Build a Sum array
        for i in range(len(arr)):
            add.append(arr[i] + arr[i-1])



if __name__ == "__main__":
    s = Solution()
    print(s.sumOddLengthSubarrays([1,4,2,5,3]))
    print(s.sumOddLengthSubarrays([1,2]))
    print(s.sumOddLengthSubarrays([10, 11, 12]))
