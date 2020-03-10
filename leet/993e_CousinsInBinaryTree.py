# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        que = deque()
        que.append((root, None))

        while que:
            sz = len(que)
            xseen, yseen = False, False
            xparent, yparent = None, None

            for i in range(sz):
                node, parent = que.popleft()
                if node.val == x:
                    xseen = True
                    xparent = parent
                elif node.val == y:
                    yseen = True
                    yparent = parent

                if node.left:
                    que.append((node.left, node))
                if node.right:
                    que.append((node.right, node))

            if xseen and yseen and xparent != yparent:
                return True

            elif (xseen and not yseen) or (yseen and not xseen):
                return False

        return False
