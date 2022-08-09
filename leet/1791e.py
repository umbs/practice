from collections import defaultdict

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        # 3 nodes case
        if len(edges) == 2:
            ans = set(edges[0]).intersection(set(edges[1]))
            return list(ans)[0]
            
        dt = defaultdict(list)
        
        # more than 3 nodes
        for edge in edges:
            u, v = edge
            dt[u].append(v)
            dt[v].append(u)
            
            # If number of edges > 2, that node is a star
            if len(dt[u]) > 2:
                return u
            
            if len(dt[v]) > 2:
                return v



"""
Following is superior solution. Got from discussion group
"""
"""
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        if edges[0][0] == edgese[1][0]:
            return edges[0][0]
        elif else[0][0] == edges[1][1]:
            return edges[0][0]
        else:
            return edges[0][1]

        # or more succintly
        return edges[0][0] == edges[1][0] || edges[0][0] == edges[1][1] ? edges [0][0] : edges[0][1]
"""
