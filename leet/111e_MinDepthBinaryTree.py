# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        que = deque()
        que.append(root)
        level = 0
        
        if root is None:
            return 0
        
        while que:
            sz = len(que)
            level += 1
            
            for i in range(sz):
                node = que.popleft()
                
                # leaf found
                if node.left is None and node.right is None:
                    return level
                
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
        
        return level
