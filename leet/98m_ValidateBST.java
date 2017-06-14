public class Solution {
    public boolean isValidBST(TreeNode node, long lo, long hi) {
        if(node==null) return true;
        if((long)node.val <= lo || (long)node.val >= hi)    return false;

        return  isValidBST(node.left, lo, (long)node.val) && isValidBST(node.right, (long)node.val, hi);
    }
    
    public boolean isValidBST(TreeNode root) {
        if(root==null)  return true;
        return isValidBST(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }
}
