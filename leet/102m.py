from collections import deque

class Solution:
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

