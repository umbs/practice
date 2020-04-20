# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        
        def dfs(leaf, node):
            if node.left is None and node.right is None:
                leaf.append(node.val)
                return
            
            if node.left:
                dfs(leaf, node.left)
            
            if node.right:
                dfs(leaf, node.right)

            return
        
        leaf1, leaf2 = list(), list()
        
        dfs(leaf1, root1)
        dfs(leaf2, root2)
        
        return leaf1 == leaf2
