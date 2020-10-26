# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def inorder(node, res):
            if not node:
                return

            inorder(node.left, res)
            res.append(node.val)
            inorder(node.right, res)

        res = list()
        inorder(root, res)

        d = res[1] - res[0]
        for i in range(1, len(res)):
            d = min(d, res[i] - res[i-1])

        return d


if __name__ == "__main__":
    # Not working for this: [90,69,null,49,89,null,52,null,null,null,null]
    # Output: 3, Expected 1
    r = TreeNode(90, TreeNode(69, TreeNode(49, None, TreeNode(52)), TreeNode(89)))
    print(Solution().minDiffInBST(r))
