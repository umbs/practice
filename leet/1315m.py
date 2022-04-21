class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, parent: TreeNode, grandP: TreeNode) -> None:
            if not node:
                return
            
            nonlocal ans
            if parent and grandP and grandP.val %2 == 0:
                ans += node.val
            dfs(node.left, node, parent)
            dfs(node.right, node, parent)
        
        ans = 0
        dfs(root, None, None)
        return ans

        
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if not root:
            return 0

        ans = 0
        stack = [(root, None)]

        while stack:
            node, parent = stack.pop()
            if node.right:
                if parent and parent.val % 2 == 0:
                    ans += node.right.val
                stack.append((node.right, node))
            if node.left:
                if parent and parent.val % 2 == 0:
                    ans += node.left.val
                stack.append((node.left, node))
        
        return ans
        
