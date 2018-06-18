'''
Binary search
'''
class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        lo = 0
        hi = len(A)-1
        while True:
            if hi-lo == 1 or hi == lo:
                return hi   # or is it lo?

            i = lo+(hi-lo)/2

            if A[i-1] < A[i] and A[i+1] < A[i]: # found
                return i
            elif A[i-1] < A[i] and A[i] < A[i+1]:
                lo = i
            elif A[i-1] > A[i] and A[i] > A[i+1]:
                hi = i

s = Solution()
print s.peakIndexInMountainArray([18,29,38,59,98,100,99,98,90])
