# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.inorder(root.left, res)
        res.append(root.val)
        self.inorder(root.right, res)
        return res
    
    def inorder(self, root: TreeNode, res: list) -> None:
        if root:
            self.inorder(root.left, res)
            res.append(root.val)
            self.inorder(root.right, res)

