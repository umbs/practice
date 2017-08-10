/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public boolean match(TreeNode s, TreeNode t) {
        if(s==null || t==null)  return s==t;
        
        return s.val==t.val && match(s.left, t.left) && match(s.right, t.right);
    }
    
    public boolean isSubtree(TreeNode s, TreeNode t) {
        if(s==null || t==null)  return s==t;
        
        boolean result = match(s, t);
        if(result)  return true;
        
        return isSubtree(s.left, t) || isSubtree(s.right, t);
    }
}
