class Solution:
    tot = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root:
            self.bstToGst(root.right)
            root.val = self.tot = self.tot + root.val
            self.bstToGst(root.left)
            
        return root

