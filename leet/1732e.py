class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        mx, cur = 0, 0
        for g in gain:
            cur += g
            mx = max(mx, cur)
        
        return mx
