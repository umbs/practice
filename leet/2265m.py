# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def util(node):
            if node.left is None and node.right is None:
                return node.val, 1, 1
            
            if node.left:
                lsum, lcount, lans = util(node.left)
            else:
                lsum, lcount, lans = 0, 0, 0
            
            if node.right:
                rsum, rcount, rans = util(node.right)
            else:
                rsum, rcount, rans = 0, 0, 0

            sum = node.val + lsum + rsum
            count = 1 + lcount + rcount
            ans = lans + rans
            
            if sum//count == node.val:
                ans += 1
            
            return sum, count, ans
        
        _, _, ans = util(root)

        return ans
        
