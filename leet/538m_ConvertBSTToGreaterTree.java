/* 
 * 538M - Convert a BST to Greater Tree.
 *
 * Greater Tree means, value at each node is a sum of all elems greater than
 * that node in BST.
 *
 * Solution: Do reverse Inorder traversal such that numbers are printed in
 * decreasing order. Sum up as you go along. For each node, replace that node
 * with the sum.
 *
 * Linear run time.
 *
 * Input: The root of a Binary Search Tree like this:
 *               5
 *             /   \
 *            2     13
 * 
 * Output: The root of a Greater Tree like this:
 *              18
 *             /   \
 *           20     13
 * */

import java.util.*;

public class Solution {
    int sum = 0;
    public void sumUtil(TreeNode node) {
        if(node == null)    return;

        sumUtil(node.right);
        node.val += sum;
        sum = node.val;
        sumUtil(node.left);
    }

    public TreeNode convertBST(TreeNode root) {
        sumUtil(root);
        return root;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
    }
}
