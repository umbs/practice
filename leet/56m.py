class Solution:
    def merge(self, vals: List[List[int]]) -> List[List[int]]:
        """
        - Have two pointers: one in results array, one in intervals array
        - examine them
            - if overlap, merge the interval with results and move forward
            - else, add the interval to results and move forward
        
                                           j
                                           v
        intervals = [[1,3],[2,6],[8,10],[15,18]]
        results = [[1,6], [8,10], [15,18]]
                                     ^
                                     i
        """
        vals.sort(); ans = [vals[0]]
        
        i, j = 0, 0
        while j < len(vals):
            lo, hi = vals[j]
            st, en = ans[i]
            
            # merge
            if en >= lo:
                ans[i] = [st, max(en, hi)]
                j += 1
            else:
                ans.append(vals[j])
                j += 1
                i += 1
        
        return ans
