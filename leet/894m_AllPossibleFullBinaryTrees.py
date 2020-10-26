# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        res = self.helper(N, deque().append(TreeNode()), [])
        return res

    def helper(N, rem, run_q, res):
        if N == 0 or (not run_q):
            res.append(list(run_q))
            return

        if len(run_q) == 2**N:
            return

        n = run_q.popleft()

        if not n:
            return

        helper(N, rem, run_q.append(None),append(None), res)
        helper(N, rem-1, run_q.append(TreeNode()),append(None), res)
        helper(N, rem-1, run_q.append(None),append(TreeNode()), res)

	return
