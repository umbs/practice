"""
Saw solution from discussion forum
"""
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        # Sort on 2nd element
        intervals.sort(key=lambda x: x[1])
        
        end, count = -pow(2, 32), 0
        for st, en in intervals:
            if st >= end:
                end = en
            else:
                count += 1
        
        return count
