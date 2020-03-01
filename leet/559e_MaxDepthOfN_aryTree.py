"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from collections import deque


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0

        q = deque()
        q.append(root)
        level = 0

        while q:
            sz = len(q)
            level += 1
            for i in range(sz):
                node = q.popleft()
                q.extend(node.children)

        return level
