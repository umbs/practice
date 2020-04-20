from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def build_tree(self, arr):
        """ Builds a binary tree and returns root node.
        @param: arr is a list of integers, serialized
        @return: an object of TreeNode. Root of the tree.
        """

        N = len(arr)
        elem = [None] * N

        for i in range(1, N):
            if elem[i] is None:
                node = TreeNode(arr[i])
                elem.append(node)
            else:
                node = elem[i]

            if 2*i < N and arr[2*i]:
                node.left = TreeNode(arr[2*i])
            if (2*i + 1) < N and arr[2*i + 1]:
                node.right = TreeNode(arr[2*i + 1])

        return elem[1]

    def print_tree(self, root):
        que = deque()
        que.append(root)

        res = []

        while que:
            sz = len(que)

            for i in range(sz):
                node = que.popleft()
                res.append(node.val)

                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

        print(res)

if __name__ == "__main__":
    s = Solution()
    root = s.build_tree([7, 1, 2, 3, None, 4, None, 5])
    s.print_tree(root)
