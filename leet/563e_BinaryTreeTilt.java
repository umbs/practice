/* 563e - Find tilt of a binary tree.
 *
 * Solution copied from discussion forums. I couldn't solve this prob.
 */
public class Solution {
    int tilt = 0;
    
    public int findTilt(TreeNode root) {
        postOrder(root);
        return tilt;
    }
    
    public int postOrder(TreeNode root) {
        if (root == null) return 0;
        int leftSum = postOrder(root.left);
        int rightSum = postOrder(root.right);
        tilt += Math.abs(leftSum - rightSum);
        return leftSum + rightSum + root.val;
    }
    
    public static void main(String[] a) {
//      Solution s = new Solution();
    }
}
