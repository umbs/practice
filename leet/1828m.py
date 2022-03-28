class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        """ Brute force.
        Optimization: 1) Sort on X-Axis
        """
        ans = [0] * len(queries)
        idx = 0
        for q in queries:
            x, y, r = q
            for p in points:
                px, py = p
                if (px-x)**2 + (py-y)**2 <= r**2:
                    ans[idx] += 1
            idx += 1
        
        return ans
