# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        que = deque() 
        que.append(root)
        while que:
            node = que.pop()
            left = node.left
            right = node.right

            node.left = right
            node.right = left

            if right:
                que.append(node.right)

            if left:
                que.append(node.left)

        return root
