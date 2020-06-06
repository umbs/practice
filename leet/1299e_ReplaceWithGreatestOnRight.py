class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        sz = len(arr)
        res = [0] * sz
        grt = -1

        for i in range(sz-1, -1, -1):
            res[i] = grt
            grt = max(grt, arr[i])

        return res
