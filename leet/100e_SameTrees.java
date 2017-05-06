/* 100e
 * Given two trees, indicate if they are same, both structurally and values at
 * each node
 * */

public class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if((p==null && q!=null) || (p!=null && q==null))    return false;
        if(p==null && q==null)  return true;
        
        return (p.val==q.val) && isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
     }
}
