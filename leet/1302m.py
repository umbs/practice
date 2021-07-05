from collections import deque
from typing import List
from pprint import pprint

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.max_depth = 0
        self.total = 0

    def deepestLeavesSum(self, root: TreeNode) -> int:
        return self.deepSumDFS(root, 0)

    def deepSumDFS(self, node: TreeNode, depth: int) -> int:
        if not node:
            return 0

        # leaf node
        if node.left is None and node.right is None:
            if self.max_depth < depth:
                self.max_depth = depth
                self.total = node.val
            elif self.max_depth == depth:
                self.total += node.val
            else:
                pass

        self.deepSumDFS(node.left, depth+1)
        self.deepSumDFS(node.right, depth+1)

        return self.total

    def deepSumBFS(self, node: TreeNode, depth: int) -> int:
        qu = deque()
        qu.append(node)
        while qu:
            add, sz = 0, len(qu)
            while sz:
                node = qu.popleft()
                add += node.val
                if node.left:
                    qu.append(node.left)
                if node.right:
                    qu.append(node.right)

                sz -= 1

        return add

