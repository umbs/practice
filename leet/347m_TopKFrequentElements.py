class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        
        ll = Counter(nums).most_common(k)
        ans = [num for num, _ in ll]        
        return ans
