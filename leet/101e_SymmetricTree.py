# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def mirror(a, b):
            if a is None and b is None:
                return True

            if a and b:
                return (a.val == b.val and mirror(a.left, b.right) and mirror(a.right, b.left))

            return False

        return mirror(root, root)
