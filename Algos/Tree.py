from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.inorder(root, res)
        return res

    def inorder(self, root: TreeNode, res: list) -> None:
        if root:
            self.inorder(root.left, res)
            res.append(root.val)
            self.inorder(root.right, res)

    # PRACTICE
    def inorderIterative(self, root: TreeNode) -> List[int]:
        res, stack = [], []

        while True:
            while root:
                stack.append(root)
                root = root.left

            if not stack:
                return res

            node = stack.pop()
            res.append(node.val)
            root = node.right

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        res = []
        self.preorder(root, res)
        return res

    def preorder(self, root: TreeNode, res: list):
        if not root:
            return

        res.append(root.val)
        self.preorder(root.left, res)
        self.preorder(root.right, res)

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        stack = deque()
        stack.append(root)
        while True:
            lst = []
            sz = len(stack)
            while sz:
                node = stack.popleft()                
                lst.append(node.val)
                sz -= 1

                if node.left:
                    stack.append(node.left)
                    
                if node.right:
                    stack.append(node.right)
                    
            res.append(lst)
            
            if len(stack) == 0:
                break
                     
        return res

