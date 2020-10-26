class Solution(object):
    def longestUnivaluePath(self, root):
        ans = [0]
        def helper(node):
            """ Find longest path with value == node.val. This is local longest
            path. Along the way, update global longest path.


                    5
                  /   \
                 4     5
                  \
                   4
                    \
                     4
            """

            if node is None:
                return 0

            l = helper(node.left)
            r = helper(node.right)

            l = (l + 1) if node.left and node.val == node.left.val else 0
            r = (r + 1) if node.right and node.val == node.right.val else 0

            # Update global longest path. What's the meaning of 'l+r'? 
            # if l == 0 or r == 0 then node.val is different than it's left or 
            # right child.
            # if one of them is non-zero then current node is part of that path.
            ans[0] = max(ans[0], l+r)

            return max(l, r)
            
        helper(root)

        return ans[0]
