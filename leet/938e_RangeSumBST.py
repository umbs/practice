class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0

        res = root.val if L <= root.val <= R else 0
        
        if L <= root.val:
            res += self.rangeSumBST(root.left, L, R)
        if root.val <= R:
            res += self.rangeSumBST(root.right, L, R)
            
        return res
