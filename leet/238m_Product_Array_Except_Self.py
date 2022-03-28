class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zeros = 1, 0
        answers = [0] * len(nums)
        
        for n in nums:
            if n == 0:
                zeros += 1
            else:
                prod *= n
        
        if zeros > 1:
            return answers
        
        for i, num in enumerate(nums):
            if zeros == 0:
                answers[i] = prod//num
            elif num == 0:
                answers[i] = prod
        
        return answers
