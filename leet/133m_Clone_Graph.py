"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        # BFS
        clones, visited, que = {}, set(), deque([node])
        
        while que:
            n = que.popleft()
            if n in visited:
                continue

            visited.add(n)

            if n not in clones:
                clones[n] = Node(n.val)
            
            for neigh in n.neighbors:
                if neigh not in clones:
                    clones[neigh] = Node(neigh.val)

                clones[n].neighbors.append(clones[neigh])
                que.append(neigh)
        
        return clones[node]
