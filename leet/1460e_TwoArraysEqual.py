class Solution(object):
    def canBeEqual(self, target, arr):
        if len(target) != len(arr):
            return False

        def reverse(arr, lo, hi):
            while lo < hi:
                tmp = arr[hi]
                arr[hi] = arr[lo]
                arr[lo] = tmp

                lo, hi = lo+1, hi-1

        lo, hi = 0, 1

        while lo < len(arr):
            # Nothing to reverse if same elements
            while lo < len(arr) and target[lo] == arr[lo]:
                lo += 1

            # End of array. All is well.
            if lo == len(arr):
                return True

            hi = lo + 1

            while hi < len(arr) and target[lo] != arr[hi]:
                hi += 1

            if hi == len(arr):
                return False

            reverse(arr, lo, hi)


        return False

# Other's solution:
# https://leetcode.com/problems/make-two-arrays-equal-by-reversing-sub-arrays/discuss/660615/C++Python-1-lines

def canBeEqual(target, arr):
    return sorted(target) == sorted(arr)


def canBeEqual2(target, arr):
    import collections
    return collections.Counter(target) == collections.Counter(arr)


if __name__ == "__main__":
    s = Solution()
    print(s.canBeEqual([1,2,3,4], [2,4,1,3]))
    print(s.canBeEqual([7], [7]))
    print(s.canBeEqual([1,12], [12,1]))
    print(s.canBeEqual([3,7,9], [3,7,11]))
    print(s.canBeEqual([1,1,1,1,1], [1,1,1,1,1]))
