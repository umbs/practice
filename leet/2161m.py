class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        ans = []

        # less numbers
        for num in nums:
            if num < pivot:
                ans.append(num)

       # equal numbers
        for num in nums:
            if num == pivot:
                ans.append(num)

       # greater numbers
        for num in nums:
            if num > pivot:
                ans.append(num)

        return ans
